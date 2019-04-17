from socket import socket
import lib.client.utils as utils
from lib.client.constants import TEMP_FILE_NAME
from threading import Thread


class Client:

    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port

        self.temp_file = None

        self.socket = socket()
        #self.socket.setblocking(0)

    def connect_to_server(self):
        self.socket.connect((self.server_ip, self.server_port))

    def bind_to_port(self):
        self.socket.bind((self.server_ip, self.server_port))
        self.socket.listen(1)

    def run(self):
        # data = self.socket.recv(1024)
        # self.socket.close()
        #
        # # self.bind_to_port()
        # # connection, address = self.socket.accept()
        # # data = connection.recv(15000000)

        #self.receive_file()
        #
        t = Thread(target=self.receive_file, args=[])
        t.start()

        self.connect_to_server()
        self.socket.send(bytes(0))


    def upload_file(self, file_name):
        self.connect_to_server()
        self.send_file(file_name)

    def send_file(self, file_name):
        file = open(file_name, 'rb')

        file_data = file.read()

        self.socket.send(file_data)
        self.socket.close()

    def receive_file(self):
        """
            Receives the file from server and saves it to the temp file
        """
        temp_file = open(TEMP_FILE_NAME, 'wb')

        encrypted_data = self.socket.recv(1024)

        self.socket.close()

        temp_file.write(encrypted_data)

        self.temp_file = temp_file

        temp_file.close()

        self.save_received_file("file1")


    def save_received_file(self, file_name):
        """
            Saves the client received file with the passed name.
            The file is retrieved from the client temporary file to which
            the passed server data was saved.
        :param file_name: the name with which the file will be saved
        """
        file = utils.create_file(file_name)

        if self.temp_file is None:
            return

        file_data = utils.get_data_from_file(self.temp_file.name)

        file.write(file_data)

        file.close()


