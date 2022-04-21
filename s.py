import socket
import pyfirmata

board = pyfirmata.Arduino('/dev/ttyUSB0')
it = pyfirmata.util.Iterator(board)
it.start()



serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 8080

host = socket.gethostname()
serversocket.bind(("192.168.43.188",port))

serversocket.listen(5)

clientsocket,addr = serversocket.accept()
print(f"Połączonko od: {str(addr)}")
board.digital[7].write(1)
while True:
    msg = "fan start" + "\r\n"
    clientsocket.send(msg.encode("ascii"))

