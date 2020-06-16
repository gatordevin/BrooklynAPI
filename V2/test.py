
from BrooklynAPI.Brooklyn import Brooklyn, CardType
from BrooklynAPI.Empire import ServoType #Import servotype class to make all types accesible from the main class
from time import sleep, monotonic

brook = Brooklyn() #No longer need to pass in COM port Brooklyn will be automaticially found
brook.set_name("SamsBrook") #You can now set a custom name to your brooklyn to distinguish it from others
print(brook.get_name()) #You an also query the name
card1 = brook.card(1) #No longer need to specify a card type it will be queried automaticially
motor = card1.motor(0) # You can now pass in the servo type when creating a new servo
servo = card1.servo(1)
#motor.set_pid_constants(0.52,0.0005,0.0, 30)


while True:
    start = monotonic()
    #motor.set_power(2,50)
    #motor.set_pid_angle(20000)
    brook.write(2,4,[])
    sleep(0.02)
    end = monotonic()
    #print()









