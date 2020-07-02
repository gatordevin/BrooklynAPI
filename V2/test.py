
from BrooklynAPI.Brooklyn import Brooklyn, CardType
from BrooklynAPI.Empire import ServoType #Import servotype class to make all types accesible from the main class
from time import sleep, monotonic

brook = Brooklyn() #No longer need to pass in COM port Brooklyn will be automaticially found
# print(brook.get_name()) #You an also query the name
# card1 = brook.card(2) #No longer need to specify a card type it will be queried automaticially
# servo = card1.servo(1, ServoType.HS785HB)
# 0
while True:
    brook.heartbeat()
    # resp = list(brook.ser.read(4))
    # print(resp)
    # resp.extend(list(brook.ser.read(resp[3]+4)))
    # print("recv:", resp, "\n")
    sleep(0.5)
    #brook.write(8, 24, [])