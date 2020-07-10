from serial import Serial

brook = Serial('/dev/ttyACM0', 9600) # Establish the connection on a specific port

while True:
    resp = brook.read(4)
    resp = [x for x in resp]
    print(resp)