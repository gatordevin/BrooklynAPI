
from BrooklynAPI.Brooklyn import Brooklyn, CardType
from BrooklynAPI.Empire import ServoType, MotorType #Import servotype class to make all types accesible from the main class
from time import sleep, monotonic

brook = Brooklyn() #No longer need to pass in COM port Brooklyn will be automaticially found
brook.set_name("Sams Brook") #You can now set a custom name to your brooklyn to distinguish it from others
print(brook.get_name()) #You an also query the name
card1 = brook.card(1) #No longer need to specify a card type it will be queried automaticially
motor = card1.motor(0, MotorType.rpm84)
#servo1 = card1.servo(1, ServoType.DF9GMS)


#motor.zero_encoder()
#motor.home(1,50)

while True:
    start = monotonic()
    #motor.read_speed()
    motor.set_power(50)
    
    #resp = brook.write(2,4,[])
    #print(resp)
    
    
    end = monotonic()
    #print(end-start)
