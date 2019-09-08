import brooklyn as brd
import time
import keyboard
import random
test = brd.Brooklyn("COM8")
test.setcard(1, brd.EMPIRE_STATE)
test.setcard(2, brd.EMPIRE_STATE)
test.setcard(3, brd.EMPIRE_STATE)
test.setcard(4, brd.EMPIRE_STATE)

test.begin()

motors = [test.getmotor(1,1),test.getmotor(1,2),test.getmotor(2,1),test.getmotor(2,2),test.getmotor(3,1),test.getmotor(3,2),test.getmotor(4,1),test.getmotor(4,2)]
servoes = [test.getservo(1, 2), test.getservo(1, 3)]


def driveMotors(val):
    for i in motors:
        i.setPWM(val)

def turnServoes(angle):
    for i in servoes:
        i.setangle(angle)

def driveMotorsTurn(val):
    motors[0].setPWM(val)
    motors[1].setPWM(val)
    motors[4].setPWM(val)
    motors[5].setPWM(val)
    motors[2].setPWM(-val)
    motors[3].setPWM(-val)
    motors[6].setPWM(-val)
    motors[7].setPWM(-val)

turnServoes(2000)
time.sleep(2)
while True:
    time.sleep(0.02)
    if keyboard.is_pressed('up'):
        driveMotors(255)
    elif keyboard.is_pressed('down'):
        driveMotors(-255)
    elif keyboard.is_pressed('left'):
        driveMotorsTurn(255)
    elif keyboard.is_pressed('right'):
        driveMotorsTurn(-255)
    else:
        driveMotors(0)
    if keyboard.is_pressed('space'):
        turnServoes(2000)
    elif keyboard.is_pressed('shift'):
        turnServoes(1000)
    if keyboard.is_pressed('e'):
        driveMotors(0)
        test.end()






'''
motor2 = test.getmotor(2)
motor3 = test.getmotor(3)
motor4 = test.getmotor(4)
motor5 = test.getmotor(5)
motor6 = test.getmotor(6)
motor7 = test.getmotor(7)
motor8 = test.getmotor(8)
while True:
    if keyboard.is_pressed('left'):  # if key 'left' is pressed
        motor1.setPWM(-100)
        motor2.setPWM(-100)
        motor3.setPWM(100)
        motor4.setPWM(100)
    elif keyboard.is_pressed('right'):  # if key 'right' is pressed
        motor1.setPWM(100)
        motor2.setPWM(100)
        motor3.setPWM(-100)
        motor4.setPWM(-100)
    elif keyboard.is_pressed('down'):  # if key 'down' is pressed
        motor1.setPWM(-100)
        motor2.setPWM(-100)
        motor3.setPWM(-100)
        motor4.setPWM(-100)
    elif keyboard.is_pressed('up'):  # if key 'up' is pressed
        motor1.setPWM(100)
        motor2.setPWM(100)
        motor3.setPWM(100)
        motor4.setPWM(100)
    else:
        motor1.setPWM(0)
        motor2.setPWM(0)
        motor3.setPWM(0)
        motor4.setPWM(0)
'''
