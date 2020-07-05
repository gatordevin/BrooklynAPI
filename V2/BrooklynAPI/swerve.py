import math
from time import sleep
class swerve:

    def __init__(self, rotation_motor1, translation_motor1):
        self.rotation_motor1 = rotation_motor1
        self.translation_motor1 = translation_motor1
        # self.rotation_motor2 = rotation_motor2
        # self.translation_motor2 = translation_motor2
        # self.rotation_motor3 = rotation_motor3
        # self.translation_motor3 = translation_motor3
        # self.rotation_motor4 = rotation_motor4
        # self.translation_motor4 = translation_motor4
    def swerve_speed_calcuator(self, throttleRaw, strafeRaw, rotateRaw):
        wheelSpeeds = [0] * 4
        temp = throttleRaw*math.cos(0) + strafeRaw*math.sin(0)
        strafeRaw = -throttleRaw*math.sin(0) + strafeRaw*math.cos(0)
        throttleRaw = temp
        #240
        #472
        A = strafeRaw-rotateRaw*(240/529.5)
        B = strafeRaw+rotateRaw*(240/529.5)
        C = throttleRaw-rotateRaw*(472/529.5)
        D = throttleRaw+rotateRaw*(472/529.5)

        LFS = math.sqrt((B*B)+(C*C))
        LBS = math.sqrt((B*B)+(D*D))
        RFS = math.sqrt((A*A)+(D*D))
        RBS = math.sqrt((A*A)+(C*C))

    
        maxVal = max(LFS, LBS, RFS, RBS)

        if(maxVal > 1):
            LFS = LFS/maxVal
            LBS = LBS/maxVal
            RFS = RFS/maxVal
            RBS = RBS/maxVal
        
        wheelSpeeds[0] = int(LFS*255)
        wheelSpeeds[1] = int(LBS*255)
        wheelSpeeds[2] = int(RFS*255)
        wheelSpeeds[3] = int(RBS*255)
        
        return wheelSpeeds

    def wheel_angle_calculations(self,throttleRaw, strafeRaw, rotateRaw):
            wheelAngles = [0] * 4
            temp = throttleRaw*math.cos(0) + strafeRaw*math.sin(0)
            strafeRaw = -throttleRaw*math.sin(0) + strafeRaw*math.cos(0)
            throttleRaw = temp
            #240
            #472
            A = strafeRaw-rotateRaw*(240/529.5)
            B = strafeRaw+rotateRaw*(240/529.5)
            C = throttleRaw-rotateRaw*(472/529.5)
            D = throttleRaw+rotateRaw*(472/529.5)

            

            RBA = (math.atan2(B,C))*180/math.pi
            RFA = (math.atan2(B,D))*180/math.pi
            LFA = (math.atan2(A,D))*180/math.pi
            LBA = (math.atan2(A,C))*180/math.pi

            wheelAngles[0] = int((RBA)*13.22)
            wheelAngles[1] = int((RFA)*13.22)
            wheelAngles[2] = int((LFA)*13.22)
            wheelAngles[3] = int((LBA)*13.22)

            
            return wheelAngles

    def run_swerve(self, throttleRaw, strafeRaw, rotateRaw):
        speeds = self.swerve_speed_calcuator(throttleRaw, strafeRaw, rotateRaw)
        # print(speeds[0])
        self.translation_motor1.set_power(speeds[0])
        # self.translation_motor2.setSpeed(speeds[1])
        # self.translation_motor3.setSpeed(speeds[2])
        # self.translation_motor4.setSpeed(speeds[3])
        angles = self.wheel_angle_calculations(throttleRaw, strafeRaw, rotateRaw)
        self.rotation_motor1.set_pid_angle(angles[0])
        # self.rotation_motor2.set_pid_angle(angles[1])
        # self.rotation_motor3.set_pid_angle(angles[2])
        # self.rotation_motor4.set_pid_angle(angles[3])



