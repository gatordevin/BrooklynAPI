from serial import Serial
import atexit
from time import sleep
from collections import namedtuple
import struct
from comms import Comms

pack = {}


brook = Serial('/dev/ttyACM0', 9600, timeout=0.1) # Establish the connection on a specific port
brook.write(bytearray([140]))
print(brook.read())

def exit_handler():
    while brook.in_waiting:
        brook.read()
    pack["header"] = 255
    pack["destination_id"] = 1
    pack["sender_id"] = 0
    pack["packed_id_1"] = 0
    pack["packet_id_2"] = 0
    pack["command"] = 140
    pack["data_length"] = 0
    pack["checksum_1"] = 0
    pack["checksum_2"] = 0
    send()

atexit.register(exit_handler)

def send():
    array = list(pack.values())
    brook.write(bytearray(array))
    print(bytearray(array))
    brook.flush()
    resp = brook.read(9)
    if(len(resp)==9):
        unpacked = struct.unpack('<BBBHbbH', resp)
        # print(unpacked)
    if(len(resp)>6):
        data_resp = brook.read(resp[6])
        unpacked = struct.unpack('<lHHHH', data_resp)
        # print(unpacked)

while True:
    pack["header"] = 255
    pack["destination_id"] = 1
    pack["sender_id"] = 0
    pack["packed_id_1"] = 0
    pack["packet_id_2"] = 0
    pack["command"] = 78
    pack["data_length"] = 0
    pack["checksum_1"] = 0
    pack["checksum_2"] = 0
    send()



