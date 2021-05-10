import socket
import sys
import pickle
import json
import metascore
import random
import threading


class myThread (threading.Thread):
    def __init__(self, threadID, name, game):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.game = game
    def run(self):
        print("NODE_SECONDARY_2>Starting Thread: " + self.name)
        threadLock.acquire() # Get lock to synchronize threads
        task(self.game)
        threadLock.release() # Free lock to release next thread


# Task to get first info
def task(i):
    time = metascore.how_long_beat(i["name"])
    if time is None:
        i['time'] = str(random.randint(3, 8)) + " Hours"    
    else:
        i['time'] = str(time)  + " Hours" 
    i['meta'] = metascore.meta(i["name"]) 
    pass


# it should be in .env
ip = 'localhost'
port = 11000
connections = 10

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = (ip, port)
print('NODE_SECONDARY_2>Starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(connections)

while True:
    # Wait for a connection
    print('\nNODE_SECONDARY_2>Waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('NODE_SECONDARY_2>Connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(8192)
            new_data = []

            try:
                new_data = pickle.loads(data)
            except EOFError:
                print("NODE_SECONDARY_2>List Emply")

            if data:
                threadLock = threading.Lock()
                piscina = [] # Pool
                
                for i in new_data:
                    print("NODE_SECONDARY_2>New Thread id: " + i['id'])
                    piscina.append(myThread(i['id'], i['name'], i))
            
                # Start
                print("NODE_SECONDARY_2>Starting threads")
                for proceso in piscina:
                    proceso.start()

                print("NODE_SECONDARY_2>Waiting for the threads to finish their work")
                for t in piscina:
                    t.join()

                print("NODE_SECONDARY_2>End of thread work")
                print('NODE_SECONDARY_2>Sending response to Node 1')
                res = pickle.dumps(new_data)
                connection.sendall(res)
                break
            else:
                print('NODE_SECONDARY_2>No data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()
