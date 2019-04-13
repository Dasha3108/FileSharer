from lib.client.client import Client
from lib.server.server import Server

SERVER_PORT = 8082
NUMBER_OF_CLIENTS = 1

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
        client.run()


if __name__ == "__main__":
    main()