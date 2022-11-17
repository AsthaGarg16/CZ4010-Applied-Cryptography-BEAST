import socket
from cryptography import CryptoUtils
from cryptography import ALPHANUMERIC

class Website:
    def __init__(self) :
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((socket.gethostname(), 4876))
        server_socket.listen(1)
        self.serverSocket = server_socket

    def start(self):
        client_socket, address = self.serverSocket.accept()
        for i in range(8):
            # Receive request
            request_encrypted = client_socket.recv(112)

            # Decrypt request
            request_decrypted = CryptoUtils.decrypt(request_encrypted)

            #404 error
            print('Decoded Request:\n', repr(request_decrypted)[2:-1], sep="")
            print('ERROR 404', repr(request_decrypted[6:28-i])[2:-1], 'NOT FOUND\n')

            for j in ALPHANUMERIC:

                request_encrypted = client_socket.recv(112)
                request_decrypted = CryptoUtils.decrypt(request_encrypted)

                # Printing Invalid requests
                print('Decoded Request:\n', repr(request_decrypted)[2:-1], sep="")
                print('Invalid HTTP request\n')
            print('\n\n')
        # Close socket
        client_socket.close()
        self.serverSocket.close()

if __name__ == '__main__':
  Website().start()


      