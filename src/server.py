import socket

host = '10.5.1.102'
port = 5000

server_socket = socket.socket()
server_socket.bind((host, port))
server_socket.listen()
