import socket

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.connect((socket.gethostname(), 8080))
pladspreference = "elbil"
s.send(bytes(pladspreference, "utf-8"))
full_msg = ''
while True:
    msg = s.recv(8)
    if not msg:
        break
    full_msg += msg.decode("utf-8")
print(full_msg)
s.close()