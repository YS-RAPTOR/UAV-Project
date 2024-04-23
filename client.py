import socket
import cv2
import threading

import socket
import threading

def receive_messages(sock):
    while True:
        data, server_address = sock.recvfrom(4096)
        print(f"\nReceived message from UDP server: {data.decode()}")

def main():
    # Define the server address and port
    server_address = ('10.1.27.171', 65000)

    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Start a thread to receive messages
        receive_thread = threading.Thread(target=receive_messages, args=(sock,))
        receive_thread.start()

        while True:
            # Allow the user to type input to send messages
            message = input("Type a message to send to UDP server: ")
            sock.sendto(message.encode(), server_address)
    except KeyboardInterrupt:
        print("\nClosing client...")
        sock.close()

if __name__ == "__main__":
    main()