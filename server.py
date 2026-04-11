import socket
from protocol import build_response, parse_request

def run_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen()

    print(f"Listening on {host}:{port}")

    while True:
        client_socket, address = server_socket.accept()
        handle_client(client_socket, address)


def handle_client(client_socket, address):
    print(f"Connected to {address}")

    response = ""

    request_text = read_request(client_socket)
    print(f"Debugging print: {request_text}")
    parsed_request = parse_request(request_text)

    # check here for parsed text validity
    if parsed_request[0] != "SPUN":
        response_text = build_response(parsed_request)
        send_response(client_socket, response_text)
        client_socket.close()

    response_text = build_response(parsed_request)
    send_response(client_socket, response_text)
    client_socket.close()


def read_request(client_socket):
    data = client_socket.recv(1024)
    decoded = data.decode("utf-8")
    return decoded


def send_response(client_socket, response_text):
    response = response_text.encode("utf-8")
    client_socket.sendall(response)

