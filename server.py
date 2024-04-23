import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("localhost", 65432)
client_socket.connect(server_address)
print("Connected to the server.")
try:
    while True:
        message = input("Enter a message to send to the server: ")
        if message.lower() == "exit":
            break

        client_socket.sendall(message.encode("utf-8"))

        data = client_socket.recv(1024)
        print("Client received:", data.decode("utf-8"))

finally:
    client_socket.close()
