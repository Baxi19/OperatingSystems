import socket
import sys
import pickle
import json


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
            data = connection.recv(2048)
            new_data = []

            try:
                new_data = pickle.loads(data)
            except EOFError:
                print("NODE_SECONDARY_1>List Emply")

            if data:
                list_games = new_data.split(sep='\\^')
                print("NODE_SECONDARY_1>Total: " + str(len(list_games)))
                for element in list_games:
                    game = element.split(sep='\\~')
                    print("Name: " + game[0] + " ,Price: " + game[1])
                    # YOUR CODE HERE!!!!
                    
                    

                #print('NODE_SECONDARY_1>Sending response to node 1')
                #connection.sendall(b'Data ready, Im Node Secundary 1')
                break
            else:
                print('NODE_SECONDARY_1>No data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()
