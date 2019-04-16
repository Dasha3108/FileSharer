import socket
from threading import Thread


class Server:

    def __init__(self, server_port):

        self.server_ip = socket.getfqdn()
        self.server_port = server_port

        self.socket = socket.socket()


    def connect_to_port(self):
        self.socket.bind((self.server_ip, self.server_port))

    def disconnect(self, connection):
        connection.close()

    def listen(self, number_of_clients):
        self.socket.listen(number_of_clients)

    def connect(self):
        connection, address = self.socket.accept()
        t = Thread(target=self.send_file, args=[connection, 'file.txt'])
        t.start()
        #return connection, address

    def send_file(self, connection, file_name):

        file = open(file_name, 'rb')

        file_data = file.read(1024)

        # TODO: encrypt data

        connection.send(file_data)

    def run(self, number_of_clients):
        self.connect_to_port()
        self.listen(number_of_clients)
        #connection, address =
        self.connect()
