import struct
import array


# Pass in list of 4 bytes, returns float
def BytesToFloat(bytes):
    return bytestovar(bytes, 'f')


# Pass in a float variable, returns list of 4 bytes
def FloatToBytes(float):
    return vartobytes(float, 'f', 4)


# Pass in list of 2 bytes, returns short
def BytesToShort(bytes):
    return bytestovar(bytes, 'H')


# Pass in short, returns list of 2 bytes
def ShortToBytes(short):
    return vartobytes(short, 'H', 2)


# Pass in list of 4 bytes, returns int
def BytesToInt(bytes):
    return bytestovar(bytes, 'I')


# Pass in int, returns list of 4 bytes
def IntToBytes(int):
    return vartobytes(int, 'I', 4)


# Packs a variable, given a data type and number of bytes
# Returns list of bytes, LSB first (little endian)
def vartobytes(data, type, numbytes):
    s = struct.Struct(type)
    packed = s.pack(data)
    data = list()
    for i in range(0,numbytes):
        data.append(int(packed[i].encode('hex'), 16))
    return data


def bytestovar(data, type):
    extract = array.array('B', data).tostring()
    s = struct.Struct(type)
    return (s.unpack(extract))[0]


def readBytes(serial, numbytes):
    data = list()
    for i in range(0, numbytes):
        data.append(serial.read())
    return data

