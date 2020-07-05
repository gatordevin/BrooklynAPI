
from BrooklynAPI.Brooklyn import Brooklyn, CardType
from BrooklynAPI.Empire import ServoType, MotorType #Import servotype class to make all types accesible from the main class
from time import sleep, monotonic
from BrooklynAPI.swerve import swerve

brook = Brooklyn() #No longer need to pass in COM port Brooklyn will be automaticially found
#print(brook.get_name()) #You an also query the name
card1 = brook.card(1) #No longer need to specify a card type it will be queried automaticially
# BR_turn = card1.motor(0, MotorType.rpm1to60)

BR_drive = card1.motor(1, MotorType.rpm1to60)
# swerve1 = swerve(BR_turn,BR_drive)
# servo = card1.servo(1, ServoType.HS785HB)
# 0
# BR_turn.zero_encoder()
# angle = 1680*2.83333

while True:
    BR_drive.set_power(200)
    # BR_turn.set_pid_angle(0)
    sleep(0.01)
    # pass
    # swerve1.run_swerve(0.5,0,0)
    # sleep(0.1)
#     brook.heartbeat()s
    # print(angle*4.25*1.55555555556)
    #BR_turn.set_pid_angle(int(angle))
    #BR_turn.read_encoder()
#     # BR_drive.set_power(50)
#     # resp = list(brook.ser.read(4))
#     # print(resp)
#     # resp.extend(list(brook.ser.read(resp[3]+4)))
#     # print("recv:", resp, "\n")
#     #brook.write(8, 24, [])
