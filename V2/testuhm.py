import serial
ser = serial.Serial(port="dev/tty",baudrate=1000000,timeout=None)
ser.write(bytearray([0,0,0,180,2,45,9,155]))
while True:
    ser.write(bytearray([180]))
    print(ord(ser.read()))