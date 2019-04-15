import socket
from threading import Thread
import lib.client.utils as utils
from lib.client.constants import TEMP_FILE_NAME


class Server:

    def __init__(self, server_port):

        self.server_ip = socket.getfqdn()
        self.server_port = server_port

        self.socket = socket.socket()

    def bind_to_port(self):
        self.socket.bind((self.server_ip, self.server_port))

    def connect_to_port(self):
        self.socket.connect((self.server_ip, self.server_port))

    def disconnect(self, connection):
        connection.close()

    def listen(self, number_of_clients):
        self.socket.listen(number_of_clients)

    def connect(self):
        connection, address = self.socket.accept()
        data = connection.recv(1024)
        if data != '':
            t = Thread(target=self.receive_file, args=[data])
            t.start()
        else:
            t = Thread(target=self.send_file, args=[connection, 'file.txt'])
            t.start()
        #return connection, address


    def run(self, number_of_clients):
        self.bind_to_port()
        self.listen(number_of_clients)
        #connection, address =
        self.connect()

    def send_file(self, connection, file_name):

        file = open(file_name, 'rb')

        file_data = file.read(1024)

        # TODO: encrypt data

        connection.send(file_data)

    def receive_file(self, data):

        #file = utils.create_file(TEMP_FILE_NAME)

        temp_file = open(TEMP_FILE_NAME, 'wb')

        encrypted_data = data   #self.socket.recv(1024)
        self.socket.close()

        # TODO: decrypt the received data
        temp_file.write(encrypted_data)

        self.temp_file = temp_file

        temp_file.close()

        self.save_received_file('file1.txt')

    def save_received_file(self, file_name):

        file = utils.create_file(file_name)

        if self.temp_file is None:
            return

        file_data = utils.get_data_from_file(self.temp_file.name)

        file.write(file_data)

        file.close()


