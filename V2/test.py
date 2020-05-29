from comms import Comm
from time import sleep

brooklyn = Comm()
while True:
    brooklyn.write(2,24,[56])