import flask
import json
from Joystick import socketJoy
from ..BrooklynAPI.Brooklyn import Brooklyn, CardType
from ..BrooklynAPI.Empire import ServoType, MotorType #Import servotype class to make all types accesible from the main class
from time import sleep, monotonic
from ..BrooklynAPI.swerve import swerve
app = flask.Flask(__name__)
joy = socketJoy()

brook = Brooklyn() #No longer need to pass in COM port Brooklyn will be automaticially found
#print(brook.get_name()) #You an also query the name
card1 = brook.card(1) #No longer need to specify a card type it will be queried automaticially
BR_turn = card1.motor(0, MotorType.rpm1to60)

BR_drive = card1.motor(1, MotorType.rpm1to60)
swerve1 = swerve(BR_turn,BR_drive)
# servo = card1.servo(1, ServoType.HS785HB)
# 0
BR_turn.zero_encoder()
# angle = 1680*2.83333

@app.route('/')
def hello():
    return flask.render_template('index.html')

@app.route('/joy_data', methods = ['POST'])
def send_emails():
    joy.update_data(flask.request.get_json())
    swerve1.run_swerve(joy.left_y,joy.left_x,joy.right_x)
    print(joy.left_bumper)
    return 'OK'

if __name__ == '__main__':
    app.run()
