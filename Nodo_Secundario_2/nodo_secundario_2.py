import socket
import sys


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
    print('NODE_SECONDARY_2>Waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('NODE_SECONDARY_2>Connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1024)
            print('NODE_SECONDARY_2>Received {!r}'.format(data))
            if data:
                # YOUR CODE HERE!!!!

                print('NODE_SECONDARY_2>Sending response to node 1')
                connection.sendall(b'Hello, Im Node Secundary 2')
            else:
                print('NODE_SECONDARY_2>No data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()
