
from BrooklynAPI.Brooklyn import Brooklyn, CardType
from BrooklynAPI.Empire import ServoType #Import servotype class to make all types accesible from the main class
from time import sleep, monotonic

brook = Brooklyn() #No longer need to pass in COM port Brooklyn will be automaticially found
brook.set_name("DevinsBrook") #You can now set a custom name to your brooklyn to distinguish it from others
print(brook.get_name()) #You an also query the name
card1 = brook.card(1) #No longer need to specify a card type it will be queried automaticially
motor = card1.motor(0)
motor.zero_encoder()
motor.set_pid_constants(0.087,0.000,0.000, 40)
while True:
    start = monotonic()
    #motor.set_power(1,50)
    #motor.read_encoder()
    #motor.set_pid_angle(-2000)

    sleep(0.02)
    end = monotonic()
    









