from time import sleep
import brooklyn as brd
import keyboard
test = brd.Brooklyn("COM8")
test.setcard(1, brd.EMPIRE_STATE)
test.setcard(2, brd.EMPIRE_STATE)
test.setcard(3, brd.EMPIRE_STATE)
test.setcard(4, brd.EMPIRE_STATE)

test.begin()

left = test.getservo(2, 1)
right = test.getservo(2, 2)
while True:
    left.setangle(1000)
    right.setangle(1000)
    sleep(6)
    left.setangle(2000)
    right.setangle(2000)
    sleep(6)
#left.setangle(1600)
#right.setangle(1600)
test.end()

