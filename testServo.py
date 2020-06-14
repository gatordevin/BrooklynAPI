import brooklyn as brd
import time

test = brd.Brooklyn("COM4")
test.setcard(1, brd.EMPIRE_STATE)
test.setcard(2, brd.EMPIRE_STATE)
test.setcard(3, brd.EMPIRE_STATE)
test.setcard(4, brd.EMPIRE_STATE)

test.begin()

servo1 = test.getservo(2, 1)
servo1.defineangle(180)
servo1.setangle(0)
time.sleep(3)
servo1.setangle(140)
time.sleep(3)
servo1.setangle(200)
time.sleep(3)
servo1.setangle(280)
time.sleep(2)
servo1.setangle(140)
time.sleep(2)
servo1.setangle(280)
test.end()