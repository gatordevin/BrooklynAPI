def decTo256(num):
    output = []
    output.append(num%255)
    output.append(num//255)
    return output
