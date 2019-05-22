import serial
import mysql.connector 
import string #enlever ?

ser = serial.Serial('/dev/serial0', 9600)

while True:
	data = ser.readline()
	if data[0]==";": #ajouter si code fonction == 1 alors ...
		print(data)
		data = data.split(";")
		add = data[1]
		tmp = data[2]
		debit = data[3]
		ser.write([123])
		#supprimer les print
		print "Save in DB"
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
		
