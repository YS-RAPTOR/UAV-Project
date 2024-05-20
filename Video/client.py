import socket
import cv2

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ("192.168.76.27", 1234)

# Capture video from the camera
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

while True:
    ret, frame = cam.read()
    if not ret:
        break

    # Base64 encode the frame
    _, buffer = cv2.imencode(".jpg", frame)
    image_bytes = buffer.tobytes()
    client_socket.sendto(image_bytes, server_address)

cam.release()
