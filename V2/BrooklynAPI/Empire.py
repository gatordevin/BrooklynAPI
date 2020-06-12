class Empire:
    def __init__(self, brook, cid):
        self.brook = brook
        self.motors = []
        self.servos = []
        self.cids = [cid+1, cid+2]

    def motor(self, mid):
        if mid is 1:
            motor = Motor(self.cids[0], self.brook)
        elif mid is 2:
            motor = Motor(self.cids[1], self.brook)
        else:
            print("invalid motor")
        self.motors.append(self.motors)
        return motor
        
    def servo(self, sid):
        if sid is 1:
            servo = Servo(self.cids[0], 1, self.brook)
        elif sid is 2:
            servo = Servo(self.cids[1], 1, self.brook)
        elif sid is 3:
            servo = Servo(self.cids[0], 0, self.brook)
        elif sid is 4:
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
        resp = self.brook.write(self.cid, 9, [self.sid, 0])

    def set_angle(self, angle):
        resp = self.brook.write(self.cid, 9, [self.sid, angle])
        print(resp)