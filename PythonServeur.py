import serial
import string
#import mysql.connector 

ser = serial.Serial('/dev/serial0', 9600)

while True:
	data = ser.readline()
	if data[0]==";":
		#print(data)
		data = data.split(";")
		add = data[1]
		tmp = data[2]
		debit = data[3]
		print "Save in DB"
		print "addresse :",add
		print "temperature :",tmp
		print "Debit :",debit

	#conn = mysql.connector.connect(host="127.0.0.1",user="root",password="raspberry", 		database="dressthing")
	#cursor = conn.cursor()

	#requete = "INSERT INTO `dressthing`.`Capteurs` (`magnetique`, `couleur`) VALUES (%s, %s)"
	#valeurs = (magnetique,couleur)
	
	#cursor.execute(requete,valeurs)

	#conn.commit()

	#conn.close()

