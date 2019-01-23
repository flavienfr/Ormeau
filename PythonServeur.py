import serial
import string

ser = serial.Serial('/dev/serial0', 9600)

while True:
	data = ser.readline()
	print(data)
	
