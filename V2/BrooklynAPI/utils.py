def decTo256(num):
    output = []
    output.append(num%255)
    output.append(num//255)
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
   num = num*1000 
   num = int(num)
   data = decTo256(num)
   return data

