import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((socket.gethostname(), 8787))

total_msg = ""
start = time.time()

while True:
    msg = s.recv(20)
    if (len(msg) <= 0):
        break
    total_msg += msg.decode("utf-8")
    if(time.time() > start):
        break

print(total_msg)
data = input("Tell me something")
s.send(bytes(data, "utf-8"))
s.close()