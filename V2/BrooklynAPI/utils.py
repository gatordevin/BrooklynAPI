import math

def negitiveCheck(num):
    if(abs(num) == num):
        return 1
    else:
        return 0

def decTo256(num):
    output = []
    temp = abs(num)
    output.append(temp%255)
    output.append(temp//255)
    output.append(negitiveCheck(num))
    return output

def interpret2(packet):
    encoder_pos = packet[4] + packet[5]*255
    if(packet[6] == 1):
        encoder_pos = encoder_pos*-1
    return encoder_pos

def interpret(packet):
    
   
    encoder_pos = packet[4]
    if(packet[5] == 1):
        encoder_pos = encoder_pos*-1
    return encoder_pos

def double_to_data(num):
    num2 = num*10000 
    num3 = int(num2)
    data = decTo256(num3)
    return data

def swerve_speed_calcuator(throttleRaw, strafeRaw, rotateRaw):
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

def wheel_angel_calculations(throttleRaw, strafeRaw, rotateRaw):
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

        wheelAngles[0] = RBA
        wheelAngles[1] = RFA
        wheelAngles[2] = LFA
        wheelAngles[3] = LBA

        
        return wheelAngles;
