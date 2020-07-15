from serial import Serial, SerialTimeoutException, SerialException
import serial.tools.list_ports
import sys
import struct
import atexit
import time
import termios

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
        self.connect_to_device(port, name, baudrate, timeout, write_timeout)
        if not self.is_open:
                print("Failed to open serial port")
                sys.exit()
        self.handshake(140)
        self.send_packet = PacketStructure()
        self.recv_packet = PacketStructure()
        self.send_packet.packet_id = 0
        atexit.register(self.exit_handler)

    def connect_to_device(self, port, name, baudrate, timeout, write_timeout):
        if port is not None:
            super().__init__(port=port, baudrate=baudrate, timeout=timeout, write_timeout=write_timeout)
            
    def reconnect_to_device(self):
        try:
            ports = list(serial.tools.list_ports.comports())
            for port in ports:
                if(port.device==self.port):
                    self.open()
                    self.handshake(140)
                    break
        except SerialException:
            print("Failed to connect to device")

    def exit_handler(self):
        try:
            while self.in_waiting:
                self.read()
            self.send_packet.destination_id = 1
            self.send_packet.command = 140
            self.send_packet.data = []
            self.write_packet()
            print(self.read_packet())
        except OSError:
            self.close()
            print("Waiting for reconnect")
            while not self.is_open:
                self.reconnect_to_device()
            
   

    def handshake(self, handshake_byte):
        self.write(bytearray([handshake_byte]))
        resp = ord(self.read(1))
        if(resp==handshake_byte):
            print("handshaked")
            return True
        else:
            print("Handshake Failed")
            sys.exit(0)
            return False

    def write_packet(self, data_type=None):
        
        data_byte_array = []
        if data_type is not None:
            data_byte_array = struct.pack('<'+data_type, *self.send_packet.data)
        else:
            data_byte_array = bytearray(self.send_packet.data)
        self.send_packet.data_length = len(data_byte_array)
        self.send_packet.generate_checksum(data_byte_array)
        byte_array = bytes(self.send_packet)
        try:
            self.reset_input_buffer()
            self.write(byte_array)
            self.write(data_byte_array)
            send_time = round(time.time())
            self.flush()
            self.send_packet.packet_id += 1
            current_time = round(time.time())
            try:
                while (self.in_waiting==0):
                    current_time = round(time.time())
                    if(self.timeout<(current_time-send_time)):
                        raise SerialTimeoutException
            except OSError:
                print("Input output failed")
        except SerialTimeoutException:
            print("write timed out")
        except termios.error:
            print("input output error")
            self.exit_handler()
        return self.send_packet.get_array() + self.send_packet.data

    def read_packet(self, data_type=None):
        try:
            self.reset_output_buffer()
            resp = self.read(len(self.recv_packet))
            if(len(resp)==len(self.recv_packet)):
                resp = struct.unpack('<BBBLbbL', resp)
                data_resp = self.read(resp[5])
                self.flushInput()
                if(len(data_resp)==resp[5]):
                    if data_type is not None:
                        data_resp = struct.unpack('<'+data_type, data_resp)
                        return list(resp)+list(data_resp)
                    else:
                        return list(resp)
                else:
                    return list(resp)
        except SerialTimeoutException:
            print("read timed out")
        except termios.error:
            print("input output error")
            self.exit_handler()
        return []
                