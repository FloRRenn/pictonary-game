import socket
HOST = "localhost"
PORT = 5555

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello this is a connection")
    data = s.recv(1024)
print("Received:", data.decode())

if __name__ == '__main__':
    pass