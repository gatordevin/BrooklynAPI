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
    num2 = num*1000 
    num3 = int(num2)
    data = decTo256(num3)
    return data

