from socket import socket
import lib.client.utils as utils
from lib.client.constants import TEMP_FILE_NAME


class Client:

    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port

        self.temp_file = None

        self.socket = socket()

    def connect_to_server(self):
        self.socket.connect((self.server_ip, self.server_port))

    def receive_file(self):
        """
            Receives the file from server and saves it to the temp file
        """
        #file = utils.create_file(TEMP_FILE_NAME)

        temp_file = open(TEMP_FILE_NAME, 'wb')

        encrypted_data = self.socket.recv(1024)
        self.socket.close()

        # TODO: decrypt the received data
        temp_file.write(encrypted_data)

        self.temp_file = temp_file

        temp_file.close()

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

    def run(self):
        self.connect_to_server()
        self.receive_file()
