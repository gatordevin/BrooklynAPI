import utils
from time import sleep
class Empire:
    def __init__(self, brook, cid):
        self.brook = brook
        self.motors = []
        self.servos = []
        self.cids = [cid+1, cid+2]

    def motor(self, mid, motor_type=None):
        if mid == 0:
            motor = Motor(self.cids[0], self.brook, motor_type)
        
        else:
            print("invalid motor")
        self.motors.append(self.motors)
        return motor
        
    def servo(self, sid, servo_type=None): #Now accepts servo type as a paramter and defaults to None so user doesnt need to pass in a type
        if sid is 1:
            servo = Servo(self.cids[0], 1, self.brook, servo_type)
        elif sid == 2:
            servo = Servo(self.cids[1], 1, self.brook, servo_type)
        elif sid == 3:
            servo = Servo(self.cids[0], 0, self.brook, servo_type)
        elif sid == 4:
            servo = Servo(self.cids[1], 0, self.brook, servo_type)
        else:
            print("invalid servo")
        self.servos.append(servo)
        return servo
    def utrasonic_sensor(self): 
        pass

class Motor:
    def __init__(self, cid, brook, motor_type, collision=False):
        self.cid = cid
        self.brook = brook
        self.motor_type = motor_type
        self.limits = []
        self.desired_speed = 0
        self.collision = collision

        if(self.motor_type != None):
            self.set_pid_constants(motor_type["kP"], motor_type["kI"], motor_type["kD"], motor_type["kZ"])
            self.set_tpr()
        else:
            self.set_pid_constants(0, 0, 0, 0)

    def set_tpr(self):
        data = utils.decTo256(self.motor_type["tpr"])
        resp = self.brook.write(self.cid, 23, data)
        print(utils.interpret(resp))

    def set_power(self, power):
        if(power == 0):
            resp = self.brook.write(self.cid, 25, [0,0])
        elif(abs(power) == power):
            resp = self.brook.write(self.cid, 25, [1,abs(power)])
        else:
            resp = self.brook.write(self.cid, 25, [2,abs(power)])
        self.desired_speed = power
        if(self.collision):
            self.collision_detect()
        #print(utils.interpret2(resp))

    def read_encoder(self):
        resp = self.brook.write(self.cid, 24,[])
        print(utils.interpret2(resp))
        return utils.interpret2(resp)

    def set_pid_angle(self, setpoint):
        data = utils.decTo256(setpoint)
        resp = self.brook.write(self.cid, 26,data)
        print(utils.interpret2(resp))
        #print(resp)

    def set_pid_constants(self, Kp, Ki, Kd, Kz):
        data = utils.double_to_data(Kp)
        data.extend(utils.double_to_data(Ki))
        data.extend(utils.double_to_data(Kd))
        data.append(Kz)
        resp = self.brook.write(self.cid, 29,data)
        print(resp)
    
    def zero_encoder(self):
        
        resp = self.brook.write(self.cid, 30, [])
        #print(resp)
    
    def home(self, direction, speed):
        self.set_power(speed)
        sleep(2)
        velocity = self.read_speed()
        while True:
            velocity = self.read_speed()
            #self.read_encoder()
            if(abs(velocity) < 150):
                break

        self.set_power(0)
        self.zero_encoder()
        

    def read_speed(self):
        resp = self.brook.write(self.cid, 27, [])
        sleep(0.2)
        print(utils.interpret2(resp))
        return utils.interpret2(resp)

    def set_pid_speed(self, speed):
        data = utils.decTo256(speed)
        resp = self.brook.write(self.cid, 28, data)
        print(utils.interpret(resp))
        self.desired_speed = speed
        if(self.collision):
            self.collision_detect()
    
    def follow(self, motor):
        self.set_pid_speed(motor.read_speed())

    def sync(self, motor):
        self.follow(motor)
        sleep(0.25)
        speeds = []
        i = 0
        while True:        
            speeds[i] = self.read_speed()
            if(i==1):
                if(abs(speeds[i] - speeds[i-1]) < 0.05 and abs(self.read_speed - motor.read_speed()) > 0.5):
                    motor.follow(self)
                    break
                i = 0
            else:
                i += 1
                
    def brake_mode(self):
        self.set_pid_speed(0)

    def collision_detect(self):
        if((abs(self.read_speed()) < 1) and (self.desired_speed != 0)):
            self.brake_mode() 

    def set_rot_limit(self, min, max):
        self.limits = [min, max]
        if(self.read_encoder < self.limits[0] or self.read_encoder > self.limits[1]):
            self.brake_mode()
        
class MotorType:
    rpm30 = {"kP": 0, "kI" : 0, "kD" : 0, "kZ" : 0, "tpr" : 0}
    rpm43 = {"kP" : 0, "kI" : 0, "kD" : 0, "kZ" : 0, "tpr" : 0}
    rpm60 = {"kP" : 0, "kI" : 0, "kD" : 0, "kZ" : 0, "tpr" : 0}
    rpm84 = {"kP" : 0.11, "kI" : 0, "kD" : 0, "kZ" : 0, "tpr" : 1428}
    rpm117 = {"kP" : 0, "kI" : 0, "kD" : 0, "kZ" : 0, "tpr" : 0}
    rpm223 = {"kP" : 0, "kI" : 0, "kD" : 0, "kZ" : 0, "tpr" : 750}
    rpm312 = {"kP" : 0, "kI" : 0, "kD" : 0, "kZ" : 0, "tpr" : 0}
    rpm435 = {"kP" : 0, "kI" : 0, "kD" : 0, "kZ" : 0, "tpr" : 0}
    rpm1150 = {"kP" : 0, "kI" : 0, "kD" : 0, "kZ" : 0, "tpr" : 0}
    rpm1620 = {"kP" : 0, "kI" : 0, "kD" : 0, "kZ" : 0, "tpr" : 0}
    

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
    HS785HB = [0, 2826, 500, 2400]
    HS322HD = [0, 201, 553, 2450]
    DF9GMS = [0, 180, 1000, 2000]
    dual_mode_servo = [0, 300, 500, 2500]
    dual_mode_servo_continuous = [0, 360, 1000, 2000]
    HS755MG = [0, 200, 570, 2400]
    HS5086WP = [0, 90, 1100, 1900]

class ultrasonic_sensor():
    pass
