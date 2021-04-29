import socket
import sys
import pickle
import json
import requests
import metascore
# Update Meta
def updateMetaGame(game):
    url = 'https://operating-systems.herokuapp.com/updateMetaDataGame'
    header = {"content-type": "application/json"}
    data = json.dumps({"games": game})
    res = requests.put(url, data=data, headers=header)
    print("NODE_SECONDARY_2>Game meta updated in server: " + res.text)

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
            data = connection.recv(2048)
            new_data = []

            try:
                new_data = pickle.loads(data)
            except EOFError:
                print("NODE_SECONDARY_2>List Emply")
            
            if data:
                list_games = new_data.split(sep='\\^')
                print("NODE_SECONDARY_2>Total: " + str(len(list_games)))
                for element in list_games:
                    game = element.split(sep='\\~')
                    print("Name: " + game[0] + " ,Price: " + game[1])
                    # YOUR CODE HERE!!!!

                    #TODO: Metadata 
                    game = {
                        "name": game[0],
                        "meta": 4
                    }
                    updateMetaGame(game)

                print('NODE_SECONDARY_2>Sending response to node 1')
                connection.sendall(b'Data ready, Im Node Secundary 2')
                break 
            else:
                print('NODE_SECONDARY_2>No data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()
