import socket
import sys
import pickle
import json
from search_games import search
import threading


class myThread (threading.Thread):
    def __init__(self, threadID, name, game):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.game = game
    def run(self):
        print("NODE_SECONDARY_1>Starting Thread: " + self.name)
        threadLock.acquire() # Get lock to synchronize threads
        task(self.game)
        threadLock.release() # Free lock to release next thread


# Task to get first info
def task(i):
    best_price = search(i['name'], i['price'])
    if (best_price != False and len(best_price)==2):
        i['price'] = "US$"+str(best_price[0]) + "  (-" + str(best_price[1]) + "%)"
        i['store'] = "Amazon"
    elif (best_price == False):
        pass
    else:
        i['price'] = i['price'] + "  (-" + str(best_price[0]) + "%)"


# it should be in .env
ip = 'localhost'
port = 10000
connections = 10

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = (ip, port)
print('NODE_SECONDARY_1>Starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(connections)

while True:
    # Wait for a connection
    print('\nNODE_SECONDARY_1>Waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('NODE_SECONDARY_1>Connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(8192)
            new_data = []

            try:
                new_data = pickle.loads(data)
            except EOFError:
                print("NODE_SECONDARY_1>List Emply")

            if data:
                #TODO: insert your code here
                threadLock = threading.Lock()
                piscina = [] # Pool
                
                for i in new_data:
                    print("NODE_SECONDARY_1>New Thread id: " + i['id'])
                    piscina.append(myThread(i['id'], i['name'], i))
            
                # Start
                print("NODE_SECONDARY_1>Starting threads")
                for proceso in piscina:
                    proceso.start()

                print("NODE_SECONDARY_1>Waiting for the threads to finish their work")
                for t in piscina:
                    t.join()

                print("NODE_SECONDARY_1>End of thread work")
                print('NODE_SECONDARY_1>Sending response to Node 1')
                res = pickle.dumps(new_data)
                connection.sendall(res)
                break
                
            else:
                print('NODE_SECONDARY_1>No data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()