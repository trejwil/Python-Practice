import socket

IP_ADDRESS - '192.168.0.1'
PORT = 139


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((IP_ADDRESS, 139))
        print(f"Port {PORT} is open and listening.")
    except:
        print(f"Failed to connect to port {PORT}.")