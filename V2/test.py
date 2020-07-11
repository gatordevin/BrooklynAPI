from comms import Comms

brook = Comms('/dev/ttyACM0')

brook.handshake(140)

brook.send_packet.destination_id = 1
brook.send_packet.sender_id = 0
brook.send_packet.packet_id = 0
brook.send_packet.command = 78
brook.send_packet.checksum = 0

while True:
    write = brook.write_packet()
    recv = brook.read_packet(data_type='<lHHHH')
    print(write, recv)