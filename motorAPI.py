import struct

import ser_util as su
import packet_util as pu
NEVEREST_3P9_PPR = 25.9
NEVEREST_20_PPR = 134.4
NEVEREST_40_PPR = 280
NEVEREST_60_PPR = 420

NEVEREST3P9 = 0
NEVEREST20 = 1
NEVEREST40 = 2
NEVEREST60 = 3

NO_FAULT = 0
CURRENT_FAULT = 1
TEMP_FAULT = 2
DOUBLE_FAULT = 3


class Motor:
    def __init__(self, ser, motor_id):
        self.ser = ser
        self.cid = motor_id - 1
        self.cw = True
        self.PIDSet = False
        self.isPID = False
        self.ppr = 0
        self.error = 0
    def send_cmd(self, cmd, cid, data):
        packetsize = len(data)
        checksum1 = packetsize ^ cid ^ cmd
        #print checksum1
        for byte in data:
            checksum1 = checksum1 ^ byte
        #print checksum1
        checksum1 = checksum1 & 0xFE
        checksum2 = (~checksum1) & 0xFE
        packet = ([0xFF, 0xFF, cmd, cid, packetsize])
        for byte in data:
            packet.append(byte)
        packet.append(checksum1)
        packet.append(checksum2)
        #print("Sent:")
        #print(packet)
        #print(checksum2)

        self.ser.write(packet)
        #a = bytearray(self.ser.read(3))
        #int_values = [x for x in a]
    def setPWM(self, pwm):
        # Do not execute if PWM is out of range or if in PID mode
        if (pwm < -255) or (pwm > 255) or self.isPID:
            return False

        # Update internal memory of direction
        if pwm < 0:
            self.cw = False
        elif pwm > 0:
            self.cw = True

        # Calculate absolute value
        pwm = abs(pwm)

        # Assemble packet and write to USB, return true for success
        #packet = pu.getPacket(0x00, self.cid, list([pwm, int(self.cw)]))
        #print list(packet)
        #print packet
        #print self.calc_checksum(list(packet))
        #self.ser.write(packet)
        self.send_cmd(0x00,self.cid,[pwm, int(self.cw)])
        #data = []
        data = []
        for i in xrange(9):
            data.append(ord(su.readBytes(self.ser, 1)[0]))
        print("Recieved: ")
        print(data)
        return True

    # Sets ppr for the motor
    # ppr -- Float value > 0
    # Function ID -- 0x15
    def setPPR(self, ppr):
        # Do not execute if PPR is out of range
        if ppr < 0:
            return False

        # Update internally
        self.ppr = ppr

        # Assemble packet and write to USB, return true for success
        packet = pu.getPacket(0x15, self.cid, su.FloatToBytes(ppr))
        self.ser.write(packet)
        return True

    # Quick-access function for NeveRest motors
    def setPPRNeveRest(self, neverest):
        # Do not execute if invalid index is passed in
        if (neverest < 0) or (neverest > 3):
            return False

        # Determine PPR and transmit to board
        if neverest == self.NEVEREST3P9:
            self.setPPR(self.NEVEREST_3P9_PPR)
        if neverest == self.NEVEREST20:
            self.setPPR(self.NEVEREST_20_PPR)
        if neverest == self.NEVEREST40:
            self.setPPR(self.NEVEREST_40_PPR)
        if neverest == self.NEVEREST60:
            self.setPPR(self.NEVEREST_60_PPR)

        return True

    # Sets current limit of motor, in mA
    # ilim -- Current Limit, as a value from 0 - 30,000, in mA
    # Function ID: 0x01
    def setCurrentLimit(self, ilim):
        # Do not execute if current limit is out of range
        if (ilim < 0) or (ilim > 30000):
            return False

        # Assemble packet and write to USB, return true for success
        packet = pu.getPacket(0x01, self.cid, su.ShortToBytes(ilim))
        self.ser.write(packet)
        return True


    # Read current motor speed in RPM
    # Function ID -- 0x02
    def getSpeed(self):
        # Assemble packet and write to USB
        packet = pu.getPacket(0x02, self.cid, list())
        self.ser.write(packet)

        # Read two bytes
        resp = su.readBytes(self.ser, 2)

        # Check if the read failed, if yes, return -1
        if pu.isEmpty(resp):
            return -1

        # If read succeeded, return rpm as short
        return su.BytesToShort(resp)

    # Get motor direction as boolean
    # Returns True for cw, False for ccw
    def getDirection(self):
        return self.cw

    # Returns motor current as short, in units of mA
    # Function ID: 0x04
    def getCurrent(self):
        # Assemble packet and write to USB
        packet = pu.getPacket(0x04, self.cid, list())
        self.ser.write(packet)

        # Read two bytes
        resp = su.readBytes(2)

        # Check if the read failed, if yes, return -1
        if pu.isEmpty(resp):
            return -1

        # If read succeeded, return current in mA as short
        return su.BytesToShort(resp)

    # Set PID constants, but does not enable PID
    # kp -- Proportionality constant, as a float
    # kd -- Derivative constant, as a float
    # ki -- Integral constant, as a float
    # Function ID: 0x05
    def setPID(self, kp, kd, ki):
        # Do not execute if any constant is negative
        if (kp < 0) or (kd < 0) or (ki < 0):
            return False

        # Convert all constants to bytes
        data = list()
        data.extend(su.FloatToBytes(kp))
        data.extend(su.FloatToBytes(kd))
        data.extend(su.FloatToBytes(ki))

        # Assemble packet and write to USB, return true for success
        packet = pu.getPacket(0x05, self.cid, data)
        self.ser.write(packet)
        return True

    # PID methods for NeveRests
    def setPIDNeveRest(self, neverest):
        # Do not execute if invalid index is passed in
        if (neverest < 0) or (neverest > 3):
            return False

        self.PIDSet = True

        if neverest == self.NEVEREST3P9:
            self.setPID(0.8, 0.2, 0.05)
        if neverest == self.NEVEREST20:
            self.setPID(0.8, 0.2, 0.05)
        if neverest == self.NEVEREST40:
            self.setPID(0.8, 0.2, 0.05)
        if neverest == self.NEVEREST60:
            self.setPID(0.8, 0.2, 0.05)

        return True

    # Disable PID
    # Internally sets to manual Mode, alerts controller
    def disablePID(self):
        self.isPID = False

        # Assemble packet and write to USB, return true for success
        packet = pu.getPacket(0x03, self.cid, list([0]))
        self.ser.write(packet)
        return True

    # Enable PID
    # Internally sets to PID Mode, alerts controller
    # Will return false if PID constants were never set
    def enablePID(self):
        if not self.PIDSet:
            return False

        self.isPID = True

        # Assemble packet and write to USB, return true for success
        packet = pu.getPacket(0x03, self.cid, list([1]))
        self.ser.write(packet)
        return True

    # Sets speed of motor, if PID is enabled, to an RPM
    # rpm -- A short indicating speed in RPM, from -65,000 to 65,000
    # Function ID -- 0x06
    def setSpeed(self, rpm):
        # Do not execute if RPM is out of bounds or not in PID mode
        if (rpm < -65000) or (rpm > 65000) or not self.isPID:
            return False

        # Update internal memory of direction
        if rpm < 0:
            self.cw = False
        elif rpm > 0:
            self.cw = True

        # Create payload
        rpm = abs(rpm)
        data = list()
        data.extend(su.ShortToBytes(rpm))
        data.append(int(self.cw))

        # Assemble packet and write to SPI, return true for success
        packet = pu.getPacket(0x06, self.cid, data)
        self.ser.write(packet)
        return True

    # Reset Encoders to 0
    # Function ID -- 0x07
    def resetEncoder(self):
        # Assemble packet and write to USB, return true for success
        packet = pu.getPacket(0x07, self.cid, list())
        self.ser.write(packet)
        return True

    # Get Encoder Ticks since reset, as an int
    # Function ID -- 0x08
    def getEncoder(self):
        # Assemble packet and write to USB
        packet = pu.getPacket(0x08, self.cid, list())
        self.ser.write(packet)

        # Read four bytes
        resp = su.readBytes(4)

        # Check if the read failed, if yes, return -1
        if pu.isEmpty(resp):
            return -1

        # Get Integer
        return su.BytesToInt(resp[0:4])

    # Rotate Motor for a fixed number of rotations at a given PWM
    # rots -- Number of rotations, as a float
    # pwm -- PWM value at which to rotate, from -255 to 255
    # Function ID -- 0x09
    def rotatePWM(self, rots, pwm):
        # Do not execute if PWM is out of range, rotations < 0, or if in PID mode
        if (pwm < -255) or (pwm > 255) or (rots < 0) or self.isPID:
            return False

        # Update internal memory of direction
        if pwm < 0:
            self.cw = False
        elif pwm > 0:
            self.cw = True

        pwm = abs(pwm)

        # Assemble payload -- pwm, then direction, then # rotations
        data = list()
        data.append(pwm)
        data.append(int(self.cw))
        data.extend(su.FloatToBytes(rots))

        # Assemble packet and write to USB, return true for success
        packet = pu.getPacket(0x09, self.cid, data)
        self.ser.write(packet)
        return True

    # Rotates a motor at a given speed for a given number of rotations
    # rots -- Number of rotations, as a float
    # rpm -- RPM value at which to rotate, from -65000 to 65000
    # Function ID: 0x0A
    def rotateSpeed(self, rots, rpm):
        # Do not execute if RPM is out of range, rotations < 0, or if not in PID mode
        if (rpm < -65000) or (rpm > 65000) or (rots < 0) or not self.isPID:
            return False

        # Update internal memory of direction
        if rpm < 0:
            self.cw = False
        elif rpm > 0:
            self.cw = True

        rpm = abs(rpm)

        # Assemble payload -- pwm, then direction, then # rotations
        data = list()
        data.extend(su.ShortToBytes(rpm))
        data.append(int(self.cw))
        data.extend(su.FloatToBytes(rots))

        # Assemble packet and write to USB, return true for success
        packet = pu.getPacket(0x0A, self.cid, data)
        self.ser.write(packet)
        return True

    # Enables Coast Mode
    # Function ID: 0x0B
    def enableCoast(self):
        # Assemble packet and write to USB, return true for success
        packet = pu.getPacket(0x0B, self.cid, list())
        self.ser.write(packet)
        return True

    # Enables Brake Mode
    # Function ID: 0x0C
    def enableBrake(self):
        # Assemble packet and write to USB, return true for success
        packet = pu.getPacket(0x0C, self.cid, list())
        self.ser.write(packet)
        return True

    # Sets Coast Speed
    # spd -- Coast Speed, in ms, 0-10000
    # Function ID -- 0x0D
    def setCoastSpeed(self, spd):
        # Do not execute if speed is out of range
        if (spd < 0) or (spd > 10000):
            return False

        # Assemble packet and write to USB, return true for success
        packet = pu.getPacket(0x0D, self.cid, su.ShortToBytes(spd))
        self.ser.write(packet)
        return True

    # Stops Motor (coasting or braking)
    # Function ID -- 0x0E
    def stop(self):
        # Assemble packet and write to USB, return true for success
        packet = pu.getPacket(0x0E, self.cid, list())
        self.ser.write(packet)
        return True

    # Get motor fault as string
    # Compare output to internal constants to ascertain fault
    # FAULT_CURRENT, NO_FAULT, TEMP_FAULT, DOUBLE_FAULT
    # Function ID -- 0x10
    def getFault(self):
        # Assemble packet and write to SPI
        packet = pu.getPacket(0x0F, self.cid, list())
        self.ser.write(packet)

        # Read one byte
        resp = su.readBytes(1)

        # Check if the read failed, if yes, return -1
        if pu.isEmpty(resp):
            return -1

        # If read succeeded, return first element, the fault state
        return resp[0]
