import serial
import mysql.connector 
import string #enlever ?

ser = serial.Serial('/dev/serial0', 9600)

while True:
	data = ser.readline()
	if data[0]==";": 
		print(data)
		data = data.split(";")
		if data[1] == "1": #0rien;1fonction;2add;3tmp;4debit
			fonction = data[1]
			add = data[2]
			tmp = data[3]
			debit = data[4]
			ser.write([123])
			#supprimer les print
			print "Save in DB"
			print "fonction :",fonction
			print "addresse :",add
			print "temperature :",tmp
			print "Debit :",debit

			conn = mysql.connector.connect(host="mysql-ormeaux.alwaysdata.net",user="ormeaux",password="G27&$Ar2", database="ormeaux_29")
			cursor = conn.cursor()
			cursor = conn.cursor()

			requete = "INSERT INTO mesures(id_bassins,temperature, debit) VALUES (%s, %s, %s)"
			valeurs = (add,tmp,debit)
	
			cursor.execute(requete,valeurs)

			conn.commit()

			conn.close()
		
