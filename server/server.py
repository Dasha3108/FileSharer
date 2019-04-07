import socket

sock = socket.socket()
host = socket.gethostname()
port = 8080
sock.bind((host, port))
sock.listen(1)
conn, addr = sock.accept()

filename = input("please, enter")
file = open(filename, 'rb')
file_data = file.read(1024)
conn.send(file_data)