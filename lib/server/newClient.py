import socket
# Import socket module


def new_client():
    s = socket.socket()  # Create a socket object
    host = socket.getfqdn()  # Ip address that the TCPServer  is there
    port = 50000  # Reserve a port for your service every new transfer wants a new port or you must wait.

    s.connect((host, port))
    s.send(bytes(0))

    with open('received_file', 'wb') as f:
        print('file opened')
        while True:
            print('receiving data...')
            data = s.recv(1024)
            print('data=%s', (data))
            if not data:
                break
            # write data to a file
            f.write(data)

    f.close()
    print('Successfully get the file')
    s.close()
    print('connection closed')


if __name__ == "__main__":
    new_client()

