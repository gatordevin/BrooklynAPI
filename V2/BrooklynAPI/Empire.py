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
        
    def servo(self, sid):
        if sid == 1:
            servo = Servo(self.cids[0], 1, self.brook)
        if sid == 2:
            servo = Servo(self.cids[1], 1, self.brook)
        if sid == 3:
            servo = Servo(self.cids[0], 0, self.brook)
        if sid == 4:
            servo = Servo(self.cids[1], 0, self.brook)
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
    def __init__(self, cid, sid, brook):
        self.cid = cid
        self.sid = sid
        self.brook = brook
        self.set_angle_range(ServoType.dual_mode_servo[0], ServoType.dual_mode_servo[1], ServoType.dual_mode_servo[2], ServoType.dual_mode_servo[3])
        #self.set_angle(0)

    def set_angle(self, angle):
        resp = self.brook.write(self.cid, 9, [self.sid, angle])
        print(resp)

    def set_angle_range(self, min_angle, max_angle, min_microseconds, max_microseconds):
        data = [self.sid]
        data.extend(utils.decTo256(min_angle))
        data.extend(utils.decTo256(max_angle))
        data.extend(utils.decTo256(min_microseconds))
        data.extend(utils.decTo256(max_microseconds))
        resp = self.brook.write(self.cid, 11, data)
        print(resp)

class ServoType:
    #servo-xyz = [values found]
    #ServoType.servo-xyz to use values found
    def __init__(self, cid, sid, brook):
        self.cid = cid
        self.sid = sid
        self.brook = brook

    HS785HB = [0, 2826, 600, 2400]
    HS322HD = [0, 201, 553, 2450]
    DF9GMS = [0, 180, 1000, 2000]
    dual_mode_servo = [0, 300, 500, 2500]