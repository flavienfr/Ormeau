import serial
import string

ser = serial.Serial('/dev/serial0', 9600)

while True:
	data = ser.readline()
	if data.find(";") > 0:
		#print(data)
		data = data.split(";")
		tmp = data[0]
		debit = data[1]
		print "Save in DB"
		print "temperature :",tmp
		print "Debit :",debit
	

