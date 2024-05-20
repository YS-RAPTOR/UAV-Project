import socket
import cv2
import numpy as np

server_address = ("192.168.137.1", 1234)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(server_address)

print(f"UDP server is listening on {server_address[0]}:{server_address[1]}")

while True:
    data, client_address = sock.recvfrom(100000)
    image_array = np.frombuffer(data, np.uint8)
    img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    cv2.imshow("Server Feed", img)

    # Manage quit
    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()
