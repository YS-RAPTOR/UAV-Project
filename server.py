import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ("localhost", 65432)
server_socket.bind(server_address)


server_socket.listen(1)

print("Server is waiting for a connection...")

connection, client_address = server_socket.accept()
print("Connection from", client_address)

try:
    while True:
        data = connection.recv(1024)
        if not data:
            break

        print("Server received:", data.decode("utf-8"))

        response = "Message received: " + data.decode("utf-8")
        connection.sendall(response.encode("utf-8"))

finally:
    connection.close()
    server_socket.close()
