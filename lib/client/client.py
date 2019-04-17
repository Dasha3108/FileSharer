from socket import socket
from threading import Thread

import lib.client.utils as utils
import lib.encryption_algorithms.rc4.rc4 as rc4
import lib.storage as storage


class Client:

    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port

        self.temp_file = None

        self.socket = socket()

    def connect_to_server(self):
        self.socket.connect((self.server_ip, self.server_port))

    def bind_to_port(self):
        self.socket.bind((self.server_ip, self.server_port))
        self.socket.listen(1)

    def run(self):
        self.connect_to_server()
        self.socket.send(bytes(0))

        t = Thread(target=self.receive_file, args=[])
        t.start()

    def upload_file(self, file_name):
        self.connect_to_server()
        self.send_file(file_name)

    def send_file(self, file_name):
        file = open(file_name, 'rb')

        file_data = file.read()

        encrypted_data = rc4.encrypt(file_data, utils.KEY)

        self.socket.send(encrypted_data)
        self.socket.close()

    def receive_file(self):
        """
            Receives the file from server and saves it to the temp file
        """
        encrypted_data = self.socket.recv(1024)
        data = rc4.decrypt(encrypted_data, utils.KEY)

        storage.save_data_to_file_in_client_storage(data, "downloaded_file.txt")

        self.socket.close()
