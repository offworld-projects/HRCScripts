import snap7
import ctypes
from datetime import datetime
import time
import csv
import psycopg2

timestamp = datetime.now()
timestampString = timestamp.strftime("%Y%m%d")
cf=open("PLC"+timestampString+".csv","x")
f = open("PLC"+timestampString+".csv","a")

client = snap7.client.Client()
client.connect("192.168.10.2", 0, 0, 102)
connected = client.get_connected()
print(connected)

#Establishing the connection
conn = psycopg2.connect(
   database="postgres", user='admin', password='administrator', host='127.0.0.1', port= '5435'
)
#Setting auto commit false
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()


while(not f.closed):
	if(connected):
		size_to_read = 2646 #taken from TIA portal, offset size
		data = (ctypes.c_uint8*size_to_read)()
		result = client.as_db_read(76, 522, size_to_read,data)
		time.sleep(0.5)
		print(result)
		csvwriter=csv.writer(f)
        csvwriter.write(result)
        #THIS NEEDS TO BE TESTED
        cursor.execute('''INSERT INTO RECIPELOGS(SEQNO, DATE, TIME, EXPNO,POSX,POSY,POSZ,USSR1,USSR2,USSR3,USSR4,MWAPPLIED,REFLECTEDPOWER,LEVELFORWARD,LEVELHIGHVOLT,ANODICCURRENT,METHANE,EXPNOTES) VALUES (result)''')

        # Commit your changes in the database
        conn.commit()
        print("Records inserted........")
	else:
		f.close()
	print(data)


