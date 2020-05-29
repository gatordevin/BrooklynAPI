import serial
import atexit
from threading import Thread 
from time import sleep

class Comm:
    def __init__(self, port='/dev/ttyACM0'):
        self.port = port
        self.ser = serial.Serial(port=self.port,baudrate=1000000)
        self.packet = []
        self.resp = []
        t = Thread(target = self.running_comms, daemon=True)
        while not self.heartbeat(): pass
        t.start()
    
    def exit_handler(self):
        self.ser.write(b"Q")

    def read_packet(self):
        recv_tmp_packet = []
        header = ord(self.ser.read())
        while header != 255:
            if(self.ser.in_waiting>0):
                header = ord(self.ser.read())
        recv_tmp_packet.append(header)
        if(header==255):
            ID = ord(self.ser.read())
            recv_tmp_packet.append(ID)
            cmd = ord(self.ser.read())
            recv_tmp_packet.append(cmd)
            datalen = ord(self.ser.read())
            recv_tmp_packet.append(datalen)
            for i in range(datalen):
                data = ord(self.ser.read())
                recv_tmp_packet.append(data)
            ck1 = ord(self.ser.read())
            ck2 = ord(self.ser.read())
            recv_tmp_packet.append(ck1)
            recv_tmp_packet.append(ck2)
        print(recv_tmp_packet)
        return(recv_tmp_packet)

    def calc_checksum(self,packet):
        packet_sum = sum(packet)
        checksum_1 = packet_sum // 256
        checksum_2 = packet_sum % 256
        
        return(checksum_1,checksum_2)

    def calc_resp_checksum(self,resp):
        packet_sum = sum(resp)
        packet_sum -= resp[resp[3]+4]
        packet_sum -= resp[resp[3]+5]
        checksum_1 = packet_sum // 256
        checksum_2 = packet_sum % 256
        
        return(checksum_1,checksum_2)

    def heartbeat(self):
        resp = self.write_packet([1,72,0])
        if(self.calc_resp_checksum(resp)[0] == resp[resp[3]+4]):
            if(self.calc_resp_checksum(resp)[1] == resp[resp[3]+5]):
                return True
        return False

    def write_packet(self,send_packet, wait_for_resp=True):
        send_packet.insert(0,255)
        checksums = self.calc_checksum(send_packet)
        send_packet.append(checksums[0])
        send_packet.append(checksums[1])
        byte_send_packet = bytearray(send_packet)
        #print(send_packet)
        self.ser.write(byte_send_packet)
        if(wait_for_resp):
            recv_packet = self.read_packet()
            return(recv_packet)

    def write(self,cid,cmd,packet):
        packet.insert(0,len(packet))
        packet.insert(0,cmd)
        packet.insert(0,cid)
        self.packet = packet
        while(self.resp == []):
            pass
        resp = self.resp
        self.resp = []
        return(resp)

    def running_comms(self):
        while True:
            if self.packet == []:
                self.heartbeat()
                pass
            else:
                self.resp = self.write_packet(self.packet)
                self.packet = []
            sleep(0.01)

#Packet Structure
#Header, ID, CMD, DataLen, Data, Checksum1, Checksum2
#User packet
#ID,CMD,DATA
