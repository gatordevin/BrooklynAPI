import flask
import json
from Joystick import socketJoy
from BrooklynAPI.Brooklyn import Brooklyn, CardType
from BrooklynAPI.Empire import ServoType, MotorType #Import servotype class to make all types accesible from the main class
from time import sleep, monotonic
from BrooklynAPI.swerve import swerve
from threading import Thread

app = flask.Flask(__name__)
joy = socketJoy()

brook = Brooklyn() #No longer need to pass in COM port Brooklyn will be automaticially found
#print(brook.get_name()) #You an also query the name
card1 = brook.card(1) #No longer need to specify a card type it will be queried automaticially
card2 = brook.card(2)
card3 = brook.card(3)
card4 = brook.card(4)
BR_turn = card1.motor(0, MotorType.rpm1to60)
FR_turn = card2.motor(0, MotorType.rpm1to60)
BL_turn = card3.motor(0, MotorType.rpm1to60)
FL_turn = card4.motor(0, MotorType.rpm1to60)

BR_drive = card1.motor(1, MotorType.rpm1to60)
FR_drive = card2.motor(1, MotorType.rpm1to60)
BL_drive = card3.motor(1, MotorType.rpm1to60)
FL_drive = card4.motor(1, MotorType.rpm1to60)
swerve1 = swerve(BR_turn,BR_drive, FR_turn, FR_drive, BL_turn, BL_drive, FL_turn, FL_drive)

# servo = card1.servo(1, ServoType.HS785HB)
# 0
BR_turn.zero_encoder()
FR_turn.zero_encoder()
BL_turn.zero_encoder()
FL_turn.zero_encoder()
# angle = 1680*2.83333


def Brooklyn_stuf(joy):
    while True:
        print(joy.left_y, joy.left_x, joy.right_x)
        if(abs(joy.left_y)<0.2):
            joy.left_y = 0
        if(abs(joy.right_y)<0.2):
            joy.right_x = 0
        
        BR_drive.set_power(int(joy.right_y)*255)
        FR_drive.set_power(int(joy.right_y)*255)
        BL_drive.set_power(int(joy.left_y)*255)
        FL_drive.set_power(int(joy.left_y)*255)

t = Thread(target=Brooklyn_stuf, args=(joy,))
t.daemon = True
t.start()

@app.route('/')
def hello():
    return flask.render_template('index.html')

@app.route('/joy_data', methods = ['POST'])
def send_emails():
    joy.update_data(flask.request.get_json())
    return 'OK'

if __name__ == '__main__':
    app.run()
