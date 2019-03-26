import serial
import string

ser = serial.Serial('/dev/serial0', 9600)

while True:
	data = ser.readline()
	if data[0]==";":
		print(data)
		data = data.split(";")
		add = data[1]
		tmp = data[2]
		debit = data[3]
		ser.write([123])
		
		print "Save in DB"
		print "addresse :",add
		print "temperature :",tmp
		print "Debit :",debit
		

