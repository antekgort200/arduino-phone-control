import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 3456
s.connect(("192.168.43.1",port))

msg = s.recv(1024)
s.close()
print(msg.decode("ascii"))
