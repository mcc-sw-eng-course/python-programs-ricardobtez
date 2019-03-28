import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 8787))
s.listen(5)

while True:
    clientSocket, address = s.accept()
    print(f"The client address is: {address}")
    clientSocket.send(bytes("Welcome to server!", "utf-8"))
    data = clientSocket.recv(20)
    print(f"Client said: {data.decode('utf-8')}")
    clientSocket.close()


s.close()