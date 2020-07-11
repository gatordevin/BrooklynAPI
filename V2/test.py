from comms import Comms

brook = Comms('/dev/ttyACM0')

brook.send_packet.destination_id = 1
brook.send_packet.command = 78
brook.send_packet.data = [-121.567, 123, -170, -4446744073709551615]

while True:
    write = brook.write_packet(data_type='fIhq')
    recv = brook.read_packet(data_type='f')
    print(write, recv)