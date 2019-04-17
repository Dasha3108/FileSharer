from lib.client.client import Client
from lib.server.server import Server

SERVER_PORT = 8082
NUMBER_OF_CLIENTS = 5

def main():
    server_port = SERVER_PORT

    server = Server(server_port)
    server_ip = server.server_ip

    client = Client(server_ip, server_port)

    choice = input("1- Server / 2- Peer\n")
    if choice == "1":
        print(server.server_ip)
        server.run(NUMBER_OF_CLIENTS)
    else:
        choice_of_client = input("1- Upload / 2- Download\n")
        if choice_of_client == "1":
            file_name = input("Input name of file\n")
            client.upload_file(file_name)
        else:
            # nclient = Client(server_ip, server_port)
            # nclient.connect_to_server()
            client.run()
            # nclient.receive_file()


if __name__ == "__main__":
    main()