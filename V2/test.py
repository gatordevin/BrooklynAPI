from BrooklynAPI.Brooklyn import Brooklyn, CardType
from time import sleep, monotonic

brook = Brooklyn(port="COM4")
card1 = brook.card(1, CardType.Empire)
servo1 = card1.servo(1)
servo2 = card1.servo(2)
servo3 = card1.servo(3)
servo4 = card1.servo(4)
while True:
    start = monotonic()
    servo1.set_angle(0)
    sleep(1)
    servo1.set_angle(180)
    sleep(1)
    end = monotonic()
    print(end-start)