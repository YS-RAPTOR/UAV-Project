import socket
import cv2

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ("localhost", 1234)

# Capture video from the camera
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = cam.read()
    if not ret:
        break

    # Show the frame
    cv2.imshow("Client Feed", frame)

    # Base64 encode the frame
    _, buffer = cv2.imencode(".jpg", frame)
    image_bytes = buffer.tobytes()
    client_socket.sendto(image_bytes, server_address)

    # Manage quit
    key = cv2.waitKey(1)
    if key == 27:
        break


cam.release()
cv2.destroyAllWindows()
