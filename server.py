import socket
import cv2
import threading

def receive_messages(sock):
    while True:
        data, client_address = sock.recvfrom(4096)
        print(f"\nReceived message from {client_address}: {data.decode()}")

def main():
    # Define the server address and port
    server_address = ('10.1.27.171', 65000)

    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the server address
    sock.bind(server_address)

    print(f"UDP server is listening on {server_address[0]}:{server_address[1]}")

    # Start a thread to receive messages
    receive_thread = threading.Thread(target=receive_messages, args=(sock,))
    receive_thread.start()

    try:
        while True:
            # Allow the user to type input to send messages
            message = input("Type a message to send to UDP client: ")
            sock.sendto(message.encode(), ('10.1.27.171', 65000))  # Replace 'localhost' with the client address if needed
    except KeyboardInterrupt:
        print("\nClosing server...")
        sock.close()

if __name__ == "__main__":
    main()
