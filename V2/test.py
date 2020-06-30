
from BrooklynAPI.Brooklyn import Brooklyn, CardType
from BrooklynAPI.Empire import ServoType, MotorType #Import servotype class to make all types accesible from the main class
from time import sleep, monotonic

brook = Brooklyn() #No longer need to pass in COM port Brooklyn will be automaticially found
brook.set_name("Sams Brook") #You can now set a custom name to your brooklyn to distinguish it from others
print(brook.get_name()) #You an also query the name
card1 = brook.card(1)

#card3 = brook.card(3) #No longer need to specify a card type it will be queried automaticially

motor1 = card1.motor(0, MotorType.rpm84)

#motor2 = card3.motor(0, MotorType.rpm84)

#motor3 = card1.motor(1, MotorType.rpm84)
#motor4 = card3.motor(1, MotorType.rpm84)



#motor.zero_encoder()
#motor.home(1,50)

while True:
    start = monotonic()
    motor1.set_power(50)
    
    #resp = brook.write(2,4,[])
    #print(resp)
    
    
    end = monotonic()
    #print(end-start)
