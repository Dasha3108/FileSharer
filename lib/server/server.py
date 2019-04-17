import socket
from threading import Thread

import lib.storage as storage


class Server:

    def __init__(self, server_port):

        self.server_ip = socket.getfqdn()
        self.server_port = server_port

        self.socket = socket.socket()

        self.temp_file = None

    def bind_to_port(self):
        self.socket.bind((self.server_ip, self.server_port))

    def disconnect(self, connection):
        connection.close()

    def listen(self, number_of_clients):
        self.socket.listen(number_of_clients)

    def connect(self):
        connection, address = self.socket.accept()
        data = connection.recv(1024)
        if data != bytes(0):
            t = Thread(target=self.receive_file, args=[data])
            t.start()
        else:
            t = Thread(target=self.send_file, args=[connection])
            t.start()

    def run(self, number_of_clients):
        self.bind_to_port()
        self.listen(number_of_clients)
        self.connect()

    def send_file(self, connection):
        file_data = storage.get_data_from_file_in_storage('uploaded_file.txt')

        connection.send(file_data)

    def receive_file(self, data):
        storage.save_data_to_file_in_storage(data, 'uploaded_file.txt')

        self.socket.close()
