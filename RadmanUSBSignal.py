import io
import time
import os
import serial
import serial.tools.list_ports

if __name__ == '__main__' :
    try :
        portlist = serial.tools.list_ports.comports()

        with serial.Serial('COM4',9600, timeout=10, bytesize=8) as ser:
            ser.write(b'\x40\x3b')
            time.sleep(.1)
            data = ser.readline()
            print(data)
            ser.write(b'\x4d\x45\x41\x53\x5f\x53\x54\x4f\x50\x5f\x43\x49\x42\x3b')
            time.sleep(.1)
            data1 = ser.readline()
            print(data1)
            ser.write(b'\x52\x45\x4d\x4f\x54\x45\x20\x4f\x4e\x3b')
            time.sleep(.1)
            data2 = ser.readline()
            print(data2)     
            ser.write(b'\x4d\x45\x41\x53\x5f\x53\x54\x41\x52\x54\x5f\x43\x49\x42\x3b')
            time.sleep(.1)
            data3 = ser.readline()
            print(data3)
            while True:
                data = ser.readline()
                time.sleep(.1)
                data+= ser.read()
                print(data)
    except :
        print('Program exit !')
        pass
    finally :
        #ser.close()
        pass