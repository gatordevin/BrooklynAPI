packet_buff = [0] * 100

packet_buff[0] = 255
packet_buff[1] = 0
packet_buff[2] = 4
packet_buff[3] = 0
packet_buff[4] = 0
packet_buff[5] = 0
packet_buff[6] = 1
packet_buff[7] = 3

size = 8+packet_buff[3]

print(packet_buff)
for x in range(100-size):
    packet_buff[x] = packet_buff[x+size]

print(packet_buff)