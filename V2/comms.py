from serial import Serial
import sys
import struct
import atexit

class PacketStructure:
    header = 255
    destination_id = 0
    sender_id = 0
    packet_id = 0
    command = 0
    data_length = 0
    checksum = 0
    data = []

    def __bytes__(self):
        packet_array = self.get_array()
        byte_array = struct.pack('<BBBLBBl', *packet_array)
        return byte_array

    def __len__(self):
        return len(bytes(self))

    def get_array(self):
        packet_array = [self.header, self.destination_id, self.sender_id, self.packet_id, self.command, self.data_length, self.checksum]
        return packet_array

    def generate_checksum(self, data_byte_array):
        checksum_list = [self.header, self.destination_id, self.sender_id, self.packet_id, self.command, self.data_length] + [x for x in data_byte_array]
        self.checksum = sum(checksum_list) 
        return sum(checksum_list)

class Comms(Serial):
    def __init__(self, port=None, name=None, baudrate=9600, timeout=0.1, write_timeout=0.1):
        if port is not None:
            super().__init__(port=port, baudrate=baudrate, timeout=timeout)
            if not self.is_open:
                print("Failed to open serial port")
                sys.exit()
        self.send_packet = PacketStructure()
        self.recv_packet = PacketStructure()
        self.send_packet.packet_id = 0
        atexit.register(self.exit_handler)

    def exit_handler(self):
        while self.in_waiting:
            self.read()
        self.send_packet.destination_id = 1
        self.send_packet.command = 140
        self.send_packet.data = []
        self.write_packet()
        print(self.read_packet())
   

    def handshake(self, handshake_byte):
        self.write(bytearray([handshake_byte]))
        resp = ord(self.read(1))
        if(resp==handshake_byte):
            return True
        else:
            print("Handshake Failed")
            sys.exit(0)
            return False

    def write_packet(self, data_type=None):
        if(self.in_waiting==0 & self.out_waiting==0):
            self.reset_input_buffer()
            data_byte_array = []
            if data_type is not None:
                data_byte_array = struct.pack('<'+data_type, *self.send_packet.data)
            else:
                data_byte_array = bytearray(self.send_packet.data)
            self.send_packet.data_length = len(data_byte_array)
            self.send_packet.generate_checksum(data_byte_array)
            byte_array = bytes(self.send_packet)
            print("writing")
            self.write(byte_array)
            self.write(data_byte_array)
            print("finished writing")
            self.flush()
            self.send_packet.packet_id += 1
            return self.send_packet.get_array() + self.send_packet.data
        else:
            return []

    def read_packet(self, data_type=None):
        if(self.in_waiting>0 & self.out_waiting==0):
            self.reset_output_buffer()
            resp = self.read(len(self.recv_packet))
            if(len(resp)==len(self.recv_packet)):
                resp = struct.unpack('<BBBLbbL', resp)
                data_resp = self.read(resp[5])
                if(len(data_resp)==resp[5]):
                    if data_type is not None:
                        data_resp = struct.unpack('<'+data_type, data_resp)
                        return list(resp)+list(data_resp)
                    else:
                        return list(resp)
                else:
                    return list(resp)
        return []
                