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
    #servo1.set_angle(0)
    #sleep(3)
    #for i in range(0,2827,1):
     #   servo1.set_angle(i)
    '''servo1.set_angle(0) #You can now send values greater than 255
    servo2.set_angle(0)
    servo3.set_angle(0)
    servo4.set_angle(0)
    sleep(4)
    servo1.set_angle(2000)
    servo2.set_angle(200)
    servo3.set_angle(200)
    servo4.set_angle(300)
    sleep(3)'''
    resp = brook.write(2, 50, [])
    print(resp)
    sleep(0.5)
    end = monotonic()
    #print(end-start)