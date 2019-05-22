
import mysql.connector 

idx = 2
tmp = 53.3
db = 0


conn = mysql.connector.connect(host="mysql-ormeaux.alwaysdata.net",user="ormeaux",password="G27&$Ar2", database="ormeaux_29")
#conn = mysql.connector.connect(host="10.160.108.85",user="ormeaux",password="password", database="ormeaux")
cursor = conn.cursor()
cursor = conn.cursor()

requete = "INSERT INTO mesures(id_bassins,temperature, debit) VALUES (%s, %s, %s)"
valeurs = (idx,tmp,db)
	
cursor.execute(requete,valeurs)

conn.commit()

conn.close()
