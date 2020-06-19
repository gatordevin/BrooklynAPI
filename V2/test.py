
from BrooklynAPI.Brooklyn import Brooklyn, CardType
from BrooklynAPI.Empire import ServoType #Import servotype class to make all types accesible from the main class
from time import sleep, monotonic

brook = Brooklyn() #No longer need to pass in COM port Brooklyn will be automaticially found
brook.set_name("KatiesBrook") #You can now set a custom name to your brooklyn to distinguish it from others
print(brook.get_name()) #You an also query the name
card1 = brook.card(1) #No longer need to specify a card type it will be queried automaticially
#servo1 = card1.servo(1, ServoType.HS785HB) # You can now pass in the servo type when creating a new servo
#servo2 = card1.servo(2, ServoType.DF9GMS)
#servo3 = card1.servo(3, ServoType.HS322HD)
#servo4 = card1.servo(4, ServoType.dual_mode_servo)
while True:
    start = monotonic()
    #motor.set_power(1,50)
    #motor.read_encoder()
    #motor.set_pid_angle(-2000)

    sleep(0.02)
    end = monotonic()
    #print(end-start)
