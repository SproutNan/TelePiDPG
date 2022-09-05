import serial

def serialInit():
    try:
        ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=0.5)
    except:
        ser = serial.Serial('/dev/ttyUSB1', 9600, timeout=0.5)
    ser.bytesize = 8
    print(ser)
    return ser

def portReceive(ser):
    return ser.readline()

def portWrite(ser, s:str):
    ser.write(bytes(s))

if __name__ == '__main__':
    ser = serialInit()
    cnt = 0
    while True:
        readStr = portReceive(ser)
        if len(str(readStr)):
            print(str(readStr))
            continue
        else:
            cnt += 1
            if (cnt >= 1000):
                portWrite(ser, 'y')
                cnt = 0
