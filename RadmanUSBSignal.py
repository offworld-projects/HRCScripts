import io
import time
import os
import serial
import serial.tools.list_ports
from datetime import datetime
import csv
import psycopg2


if __name__ == '__main__' :

    timestamp = datetime.now()
    timestampString = timestamp.strftime("%Y%m%d")
    cf=open("Radman"+timestampString+".csv","x")
    f = open("Radman"+timestampString+".csv","a")

    #Establishing the connection
    conn = psycopg2.connect(
       database="postgres", user='admin', password='administrator', host='127.0.0.1', port= '5435'
    )
    #Setting auto commit false
    conn.autocommit = True

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

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
            while True and not f.closed:
                data = ser.readline()
                time.sleep(.1)
                data+= ser.read()
                print(data)
                csvwriter=csv.writer(f)
                csvwriter.write(ser.readline)
                cursor.execute('''INSERT INTO EMFRADMAN(ID, DATETIME, VALUE) VALUES (datetime.now(), ser.readline)''')

                # Commit your changes in the database
                conn.commit()
                print("Records inserted........")
    except :
        print('Program exit !')
        pass
    finally :
        f.close()
        pass