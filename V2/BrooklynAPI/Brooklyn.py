from threading import Thread 
from time import sleep, monotonic
import serial
import atexit
from BrooklynAPI.Empire import Empire as empire_card
import serial.tools.list_ports
import sys
class Brooklyn:
    def __init__(self, port=None, name=None): #COM port will now be autoamtically found first avaiable arduino plugged in will be connected to if None is passed in
        self.port = port
        self.ser = None
        if(port == None):
            ports = list(serial.tools.list_ports.comports(True))
            for p in ports:
                if("Arduino" in p.description):
                    self.port = p.device
                    if(name != None):
                        self.ser = serial.Serial(port=self.port,baudrate=1000000,timeout=None)
                        self.ser.write(bytearray([140]))
                        self.ser.flush()
                        self.ser.read(1)
                        resp  = self.write(1,2,[])
                        board_name = "".join(map(chr, resp[4:-2]))
                        if board_name == name:
                            break
                        else:
                            self.ser.write(bytearray([170]))
                            self.ser.close()
                            self.ser = None
                    else:
                        break
            if(name != None):
                if(self.ser == None):
                    print("No Brooklyn with name", name, "found")
                    sys.exit(0)
        if self.port is not None:
            if(self.ser == None):
                self.ser = serial.Serial(port=self.port,baudrate=1000000,timeout=None)
                self.ser.write(bytearray([140]))
                self.ser.flush()
                self.ser.read(1)
        else:
            print("No Brooklyn Found")
            sys.exit(0)
        
        self.cards = [None,None,None,None]
        atexit.register(self.end)
        
    def end(self):
        print("Returning Brooklyn to idle mode")
        self.write(2,25,[0,0])
        self.ser.write(bytearray([170]))
        self.ser.close()
        print("Programmed ended gracefully.")

    def card(self, cid, card_type=None):
        if card_type is None:
            resp = self.write(cid+1,3,[])
            card_type = CardType.ids[resp[4]-1]
        card = card_type(self, cid)
        self.cards[cid-1] = card
        return card

    def set_name(self, name):
        buff = []
        for c in name:
            buff.append(ord(c))
        resp = self.write(1,1,buff)

    def get_name(self):
        resp  = self.write(1,2,[])
        board_name = "".join(map(chr, resp[4:-2]))
        return board_name
    
    def write(self,cid,cmd,packet_data):
        packet = [255]
        packet.append(cid)
        packet.append(cmd)
        packet.append(len(packet_data))
        packet.extend(packet_data)
        packet_sum = sum(packet)
        packet.append(packet_sum // 256)
        packet.append(packet_sum % 256)
        #print("sent:", packet)
        byte_send_packet = bytearray(packet)
        self.ser.write(byte_send_packet)
        self.ser.flush()
        resp = list(self.ser.read(4))
        resp.extend(list(self.ser.read(resp[3]+2)))
        #print("recv:", resp, "\n")
        return resp



class CardType:
    Empire = empire_card
    ids = [Empire]