from comms import Comms
from time import sleep

brook = Comms('/dev/ttyACM0')

brook.handshake(140)

brook.send_packet.destination_id = 1
brook.send_packet.command = 78
brook.send_packet.data = [-121.567, 123, -170, -4446744073709551615]

while True:
    write = brook.write_packet(data_type='fIhq')
    # print("Writing: ", write)
    recv = brook.read_packet(data_type='iHHHH')
    # print("Recieving: ", write)