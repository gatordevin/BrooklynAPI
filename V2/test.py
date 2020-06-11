from comms import Comm
from time import sleep, monotonic

brooklyn = Comm(port="/dev/ttyACM0")
while True:
    start = monotonic()
    resp = brooklyn.write(2,9,[0,0])
    # sleep(1)
    # resp = brooklyn.write(2,9,[0,180])
    end = monotonic()
    print(end-start)
    print(resp)