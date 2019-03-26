
import mysql.connector 


tmp = 25.0
db = 1.3


#conn = mysql.connector.connect(host="ormeaux-29.mysql.database.azure.com",user="ormeaux@ormeaux-29",password="Password29", database="ormeaux")
conn = mysql.connector.connect(host="10.160.108.85",user="ormeaux",password="password", database="ormeaux")
cursor = conn.cursor()
cursor = conn.cursor()

requete = "INSERT INTO `ormeaux`.`mesures` (`temppinerature`, `debit`) VALUES (%s, %s)"
valeurs = (tmp,db)
	
cursor.execute(requete,valeurs)

conn.commit()

conn.close()