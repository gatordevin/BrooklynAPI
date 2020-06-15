from BrooklynAPI.Brooklyn import Brooklyn, CardType
from BrooklynAPI.Empire import ServoType #Import servotype class to make all types accesible from the main class
from time import sleep, monotonic

brook = Brooklyn(name="DevinsBrook") #No longer need to pass in COM port Brooklyn will be automaticially found
brook.set_name("DevinsBrook") #You can now set a custom name to your brooklyn to distinguish it from others
print(brook.get_name()) #You an also query the name
card1 = brook.card(1) #No longer need to specify a card type it will be queried automaticially
servo1 = card1.servo(1, ServoType.DF9GMS) # You can now pass in the servo type when creating a new servo
servo2 = card1.servo(1, ServoType.DF9GMS)
servo3 = card1.servo(3)
servo4 = card1.servo(4)
while True:
    start = monotonic()
    servo1.set_angle(0)
    sleep(0.5)
    servo1.set_angle(200) #You can now send values greater than 255
    sleep(0.5)
    end = monotonic()
    print(end-start)