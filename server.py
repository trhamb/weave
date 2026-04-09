import socket

HOST = "127.0.0.1"
PORT = 7777

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Listening on {HOST}:{PORT}...")

while True:
    client_socket, address = server_socket.accept()
    print(f"Connection from {address}")

    data = client_socket.recv(1024)
    decoded = data.decode("utf-8")

    print(decoded)

    client_socket.close()
