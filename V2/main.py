from serial import Serial
import atexit
from time import sleep


brook = Serial('/dev/ttyACM0', 9600, timeout=0.1) # Establish the connection on a specific port
brook.write(bytearray([140]))
brook.read(140)

def exit_handler():
    while brook.in_waiting:
        brook.read()
    brook.write(bytearray([255,1,140,120]))
    resp = brook.read(4)
    resp = [x for x in resp]
    print(resp)

atexit.register(exit_handler)

def send(array):
    brook.write(bytearray(array))
    brook.flush()
    resp = brook.read(4)
    resp = [x for x in resp]
    print(resp)

while True:
    send([255,1,78,120])
    sleep(1)
    send([253,1,78,120])
    sleep(1)    



