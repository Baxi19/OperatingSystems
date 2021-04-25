import socket, pickle
import sys


class Socket_Client:
    def __init__(self, ip, port, data):
        self.ip = ip
        self.port = port
        self.data = data

    def send(self):
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        server_address = (self.ip, self.port)
        print('NODE_1>Connecting to {} port {}'.format(*server_address))
        sock.connect(server_address)

        try:
            # Send data
            sock.sendall(self.data)
            print('NODE_1>Data Sended by sockets')
            
            """
            # Look for the response
            amount_received = 0
            amount_expected = len(self.data)

            
            while amount_received < amount_expected:
                data = sock.recv(2048)
                amount_received += len(data)
                print('NODE_1>Received {!r}'.format(data))
            """

        finally:
            print('NODE_1>Closing socket')
            sock.close()
