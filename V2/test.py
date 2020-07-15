from comms import Comms
from time import monotonic, sleep
brook = Comms('/dev/ttyACM0')

brook.send_packet.destination_id = 2
brook.send_packet.command = 7
brook.send_packet.data = [-121.567, 123, -170]
wrong = 0
while True:
    start = monotonic()
    write = brook.write_packet(data_type='fIh')
    recv = brook.read_packet(data_type='h')
    end = monotonic()
    # print(1/(end-start))
    print(write)
    print(recv)