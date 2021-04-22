import socket, pickle
import sys


# it should be in .env
ip = 'localhost'
port = 10000
connections = 5

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
    print('NODE_SECONDARY_1>Waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('NODE_SECONDARY_1>Connection from', client_address)
        
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1024)
            print('NODE_SECONDARY_1>Received {!r}'.format(data))
            if data:
                # YOUR CODE HERE!!!!
                # data_arr = pickle.loads(data)
                # print(repr(data_arr))

                print('NODE_SECONDARY_1>Sending response to node 1')
                connection.sendall(b'Hello, Im Node Secundary 1')
            else:
                print('NODE_SECONDARY_1>No data from', client_address)
                break
        
        """
        while 1:
            data = connection.recv(1024)
            if not data: break
            connection.send(data)
        print("Recibido: ")
        """


    finally:
        # Clean up the connection
        connection.close()
