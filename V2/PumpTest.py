from BrooklynAPI.Brooklyn import Brooklyn, CardType
from BrooklynAPI.Empire import ServoType, MotorType #Import servotype class to make all types accesible from the main class
from time import sleep, monotonic

brook = Brooklyn() #No longer need to pass in COM port Brooklyn will be automaticially found
card1 = brook.card(1)

motor_1 = card1.motor(0)
motor_2 = card1.motor(1)

while True:
    brook.heartbeat()