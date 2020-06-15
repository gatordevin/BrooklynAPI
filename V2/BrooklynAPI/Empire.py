from BrooklynAPI import utils
class Empire:
    def __init__(self, brook, cid):
        self.brook = brook
        self.motors = []
        self.servos = []
        self.cids = [cid+1, cid+2]

    def motor(self, mid):
        if mid == 1:
            motor = Motor(self.cids[0], self.brook)
        elif mid == 2:
            motor = Motor(self.cids[1], self.brook)
        else:
            print("invalid motor")
        self.motors.append(self.motors)
        return motor
        
    def servo(self, sid, servo_type=None): #Now accepts servo type as a paramter and defaults to None so user doesnt need to pass in a type
        if sid is 1:
            servo = Servo(self.cids[0], 1, self.brook, servo_type)
        elif sid is 2:
            servo = Servo(self.cids[1], 1, self.brook, servo_type)
        elif sid is 3:
            servo = Servo(self.cids[0], 0, self.brook, servo_type)
        elif sid is 4:
            servo = Servo(self.cids[1], 0, self.brook, servo_type)
        else:
            print("invalid servo")
        self.servos.append(servo)
        return servo

class Motor:
    def __init__(self, cid, brook):
        self.cid = cid
        self.brook = brook

    def set_power(self, power):
        if(power > 1): power = 1
        if(power < -1): power = -1

        if(power == 0):
            direction = 0
        elif(power > 0):
            direction = 1
        elif(power < 0):
            direction = 2

        resp = self.brook.write(self.cid, 25, [direction,255*abs(power)])
        print(resp)


class Servo:
    def __init__(self, cid, sid, brook, servo_type): #Servo class now takes servo type as a paramter as well to allow for init servo settings
        self.cid = cid
        self.sid = sid
        self.brook = brook
        if(servo_type!=None): #Checks to see if no servo type was sent before settign angle range
            self.set_angle_range(servo_type[0], servo_type[1], servo_type[2], servo_type[3]) #If there is a servo type set angle range to the defaults
        #self.set_angle(0)

    def set_angle(self, angle):
        data = [self.sid]
        data.extend(utils.decTo256(angle)) #Set angle can now send values greater than 255 to the empire board to supprot wider range servos
        resp = self.brook.write(self.cid, 9, data)

    def set_angle_range(self, min_angle, max_angle, min_microseconds, max_microseconds):
        data = [self.sid]
        data.extend(utils.decTo256(min_angle))
        data.extend(utils.decTo256(max_angle))
        data.extend(utils.decTo256(min_microseconds))
        data.extend(utils.decTo256(max_microseconds))
        resp = self.brook.write(self.cid, 11, data)

class ServoType:
    HS785HB = [0, 2826, 600, 2400]
    HS322HD = [0, 201, 553, 2450]
    DF9GMS = [0, 180, 1000, 2000]
    dual_mode_servo = [0, 300, 500, 2500]
