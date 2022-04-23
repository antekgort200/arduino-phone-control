import socket
import pyfirmata

board = pyfirmata.Arduino("/dev/ttyUSB0")
it = pyfirmata.util.Iterator(board)
it.start()


s = socket.socket()
print("Sock made")

port = 34567
s.bind(('',port))
s.listen(5)
print("listening")
i = 0
while True:
    c,addr = s.accept()
    print("connected ",addr)
    i +=1
    c.send(b"TEST")
    c.close()
    if i % 2 == 0:
        board.digital[7].write(1)
        print("on")
    else:
        print("off")
        board.digital[7].write(0)

