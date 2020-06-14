import packet_util as pu
import ser_util as su


class Servo:

    # ser = Serial Console Object
    # cid = Component ID (1-8)
    # sid = Servo ID -- Servo 1 or Servo 2
    def __init__(self, ser, cid, sid):
        self.cid = cid - 1
        self.sid = sid
        self.ser = ser
    def send_cmd(self, cmd, cid, data):
        packetsize = len(data)
        checksum1 = packetsize ^ cid ^ cmd
        for byte in data:
            checksum1 = checksum1 ^ byte
        checksum1 = checksum1 & 0xFE
        checksum2 = (~checksum1) & 0xFE
        packet = ([0xFF, 0xFF, cmd, cid, packetsize])
        for byte in data:
            packet.append(byte)
        packet.append(checksum1)
        packet.append(checksum2)
        #print("Sent:")
        #print(packet)

        self.ser.write(packet)
        #a = bytearray(self.ser.read(5))
        #for x in a:
        #    print(str(x))
    # Sets servo angle attribute

    def setangle(self, angle):
        # Do not execute if angle is out of range or servo is continuous


        # Convert to proper angle range (0 to 180)
        #newangle = int(round(angle * (180.0/float(self.angle))))
        LSB = 0x00ff & angle
        MSB = (0xff00 & angle) >> 8
        # 0x10 for Servo 1, 0x12 for Servo 2
        pack_sid = 0x10
        if self.sid == 2:
            pack_sid = 0x12

        # Assemble packet and write to USB, return true for success
        #print("settign servo")
        self.send_cmd(pack_sid, self.cid, list([LSB,MSB]))
        data = []
        for i in xrange(9):
            data.append(ord(su.readBytes(self.ser, 1)[0]))
        print("Recieved: ")
        print(data)
        return True

    # Set Speed for continuous servo
    # Speed -- a value from -90 to 90, indicating both direction and speed
    # Function ID: 0x11/0x13 (Servo1/Servo2)
    def setspeed(self, speed):
        # Do not execute if speed is out of range or servo is not continuous

        # On motor board, 0 = full reverse, 90 is stop, 180 is full forward
        # Add 90 to produce this result given a -90 to 90 range
        data = list([speed + 90])

        # 0x11 for Servo 1, 0x13 for Servo 2
        pack_sid = 0x11
        if self.sid == 2:
            pack_sid = 0x13

        # Assemble packet and write to USB, return true for success
        packet = pu.getPacket(pack_sid, self.cid, data)
        self.ser.write(packet)
        return True
