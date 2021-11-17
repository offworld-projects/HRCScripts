import snap7
import ctypes
from datetime import datetime
import time


timestamp = datetime.now()
timestampString = timestamp.strftime("%Y%m%d")
cf=open("PLC"+timestampString+".csv","x")
f = open("PLC"+timestampString+".csv","a")

client = snap7.client.Client()
client.connect("192.168.10.2", 0, 0, 102)
connected = client.get_connected()
print(connected)

while(not f.closed):
	if(connected):
		size_to_read = 2646 #taken from TIA portal, offset size
		data = (ctypes.c_uint8*size_to_read)()
		result = client.as_db_read(76, 522, size_to_read,data)
		time.sleep(0.5)
		print(result)
	else:
		f.close()
	print(data)


