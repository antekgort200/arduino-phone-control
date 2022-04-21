import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 3456
s.connect(("ip of arduino/PC connected to arduino",port))

msg = s.recv(1024)
s.close()
print(msg.decode("ascii"))
