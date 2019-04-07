import socket


class Server:

    def __init__(self, server_port):

        self.server_ip = socket.getfqdn()
        self.server_port = server_port

        self.socket = socket.socket()


    def connect_to_port(self):
        self.socket.bind((self.server_ip, self.server_port))

    def listen(self):

        self.socket.listen()

        connection, address = self.socket.accept()


    def send_file(self, connection, file_name):

        file = open(file_name, 'rb')

        file_data = file.read(1024)

        # TODO: encrypt data

        connection.send(file_data)
