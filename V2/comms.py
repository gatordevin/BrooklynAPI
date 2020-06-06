from threading import Thread 
from time import sleep, monotonic
import serial

class Comm:
    def __init__(self, port='/dev/ttyACM0'):
        self.ser = serial.Serial(port=port,baudrate=1000000,timeout=None)

    def write(self,cid,cmd,packet_data):
        packet = [255]
        packet.append(cid)
        packet.append(cmd)
        packet.append(len(packet_data))
        packet.extend(packet_data)
        packet_sum = sum(packet)
        packet.append(packet_sum // 256)
        packet.append(packet_sum % 256)

        byte_send_packet = bytearray(packet)
        self.ser.write(byte_send_packet)
        self.ser.flush()
        resp = list(self.ser.read(4))
        resp.extend(list(self.ser.read(resp[3]+2)))
        return resp