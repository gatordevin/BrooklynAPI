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
        byte_array = struct.pack('<BBBLBBH', *packet_array)
        return byte_array

    def __len__(self):
        return len(bytes(self))

    def get_array(self):
        packet_array = [self.header, self.destination_id, self.sender_id, self.packet_id, self.command, len(self.data), self.checksum]
        return packet_array

class Comms(Serial):
    def __init__(self, port=None, name=None, baudrate=9600, timeout=0.1):
        if port is not None:
            super().__init__(port=port, baudrate=baudrate, timeout=timeout)

        self.send_packet = PacketStructure()
        self.recv_packet = PacketStructure()
        self.send_packet.packet_id = 0
        atexit.register(self.exit_handler)

    def exit_handler(self):
        while self.in_waiting:
            self.read()
        self.send_packet.destination_id = 1
        self.send_packet.sender_id = 0
        self.send_packet.command = 140
        self.send_packet.checksum = 0
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
        byte_array = bytes(self.send_packet)
        self.write(byte_array)
        data_byte_array = []
        if data_type is not None:
            data_byte_array = struct.pack(data_type, *self.send_packet.data)
        else:
            data_byte_array = bytearray(self.send_packet.data)
        self.write(data_byte_array)
        self.flush()
        self.send_packet.packet_id += 1
        return self.send_packet.get_array() + [x for x in data_byte_array]

    def read_packet(self, data_type=None):
        resp = self.read(len(self.recv_packet))
        if(len(resp)==len(self.recv_packet)):
            resp = struct.unpack('<BBBLbbH', resp)
            data_resp = self.read(resp[5])
            if(len(data_resp)==resp[5]):
                if data_type is not None:
                    data_resp = struct.unpack(data_type, data_resp)
                    return list(resp)+list(data_resp)
                else:
                    return list(resp)
            else:
                return list(resp)
        return []
                