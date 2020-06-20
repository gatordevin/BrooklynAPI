import math

class swerve:
    def swerve_speed_calcuator(self, throttleRaw, strafeRaw, rotateRaw):
        wheelSpeeds = []
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

        if(max > 1):
            LFS = LFS/maxVal
            LBS = LBS/maxVal
            RFS = RFS/maxVal
            RBS = RBS/maxVal
        
        wheelSpeeds[0] = LFS*255
        wheelSpeeds[1] = LBS*255
        wheelSpeeds[2] = RFS*255
        wheelSpeeds[3] = RBS*255
        
        return wheelSpeeds

    def wheel_angel_calculations(self,throttleRaw, strafeRaw, rotateRaw):
            wheelAngles = []
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

            wheelAngles[0] = int(RBA*3.9667*4.25)
            wheelAngles[1] = int(RFA*3.9667*4.25)
            wheelAngles[2] = int(LFA*3.9667*4.25)
            wheelAngles[3] = int(LBA*3.9667*4.25)

            
            return wheelAngles
