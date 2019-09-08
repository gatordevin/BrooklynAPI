import cardAPI
import serial
import math

EMPIRE_STATE = 1


class Brooklyn:
    def __init__(self, port='/dev/ttyACM0'):
        self.port = port
        self.ser = serial.Serial(
            port=self.port,
            baudrate=1000000
        )

        self.enabled = False

        # Declare all bays as empty
        self.card1 = None
        self.card2 = None
        self.card3 = None
        self.card4 = None

    def setcard(self, bay, card):
        # If a legitimate card, make instance for given bay.
        if card == EMPIRE_STATE:
            card_obj = cardAPI.EmpireState(bay, self.ser)
        else:
            return None

        # Assign instance to proper attribute of brooklyn
        if bay == 1:
            self.card1 = card_obj
        elif bay == 2:
            self.card2 = card_obj
        elif bay == 3:
            self.card3 = card_obj
        elif bay == 4:
            self.card4 = card_obj
        else:
            return None

    def begin(self):
        handshake = False

        # Conduct basic handshake, repeat until complete
        self.ser.write(bytearray([170]))
        while not handshake:
            if ord(self.ser.read()) == 170:
                handshake = True

        self.enabled = True
        return True

    def end(self):
        self.ser.write(bytearray([255,255,255]))
        self.enabled = False
        return True

    # Returns motor object given a motor number
    # motornum -- Must be a value from 1-8
    def getmotor(self, bay, motornum):
        if not self.enabled:
            return None

        # Return None if invalid bay.
        if bay < 0 or bay > 4:
            return None

        # Return None if invalid servo.
        if motornum < 0 or motornum > 4:
            return None

        # Return servo from appropriate card bay
        if bay == 1:
            print("Empire 1")
            return self.card1.getMotor(motornum)
        elif bay == 2:
            print("Empire 2")
            return self.card2.getMotor(motornum)
        elif bay == 3:
            print("Empire 3")
            return self.card3.getMotor(motornum)
        elif bay == 4:
            print("Empire 4")
            return self.card4.getMotor(motornum)
        else:
            return None

    # Returns servo object given a bay and servo number
    # bay -- Must be a value from 1-4
    # servonum -- Must be a value from 1-4
    def getservo(self, bay, servonum):
        if not self.enabled:
            return None

        # Return None if invalid bay.
        if bay < 0 or bay > 4:
            return None

        # Return None if invalid servo.
        if servonum < 0 or servonum > 4:
            return None

        # Return servo from appropriate card bay
        if bay == 1:
            return self.card1.getServo(servonum)
        elif bay == 2:
            return self.card2.getServo(servonum)
        elif bay == 3:
            return self.card3.getServo(servonum)
        elif bay == 4:
            return self.card4.getServo(servonum)
        else:
            return None
