#fichier = open("/etc/dhcpcd.conf", "r")

#Configuration statique
def LireIpStatique() :
	fichierR = open("/home/pi/ormeau/web/mainapp/dhcptest.conf", "r")
	contenu = fichierR.read()

	ipdebut = contenu.find("static ip_address=")
	ipdebut += 18
	i = 0
	ip = ""
	while contenu[ipdebut+i] != "/":
		ip += contenu[ipdebut+i]
		i+=1
	ipfin = ipdebut+i+1
	masque = contenu[ipfin:ipfin+2]

	fichierR.close()
	return (ip, masque, ipdebut, ipfin)

def ChangerIPstatique(newip, newmasque):
	fichierR = open("/home/pi/ormeau/web/mainapp/dhcptest.conf", "r")
	contenu = fichierR.read()

	ip, masque, ipdebut, ipfin = LireIpStatique()
	newip += "/" + newmasque
	ip = ip + "/" + masque
	contenu = contenu.replace(ip, newip)

	fichierR.close()
	fichierW = open("/home/pi/ormeau/web/mainapp/dhcptest.conf", "w")
	fichierW.write(contenu)
	fichierW.close()

def LireIprouters() :
	fichierR = open("/home/pi/ormeau/web/mainapp/dhcptest.conf", "r")
	contenu = fichierR.read()

	ipdebut = contenu.find("static routers=")
	ipdebut += 15
	i = 0
	ip = ""
	while contenu[ipdebut+i] != "#":
		ip += contenu[ipdebut+i]
		i+=1
	ipfin = ipdebut+i+1

	fichierR.close()
	return (ip, ipdebut, ipfin)

def ChangerIProuters(newiprouter):
	fichierR = open("/home/pi/ormeau/web/mainapp/dhcptest.conf", "r")
	contenu = fichierR.read()

	ip, ipdebut, ipfin = LireIprouters()
	contenu = contenu.replace(ip, newiprouter)

	fichierR.close()
	fichierW = open("/home/pi/ormeau/web/mainapp/dhcptest.conf", "w")
	fichierW.write(contenu)
	fichierW.close()


#Configuration dynamique

ip, masque, ipdebut, ipfin = LireIpStatique()
print ("Votre adresse ip :",ip,"Masque :",masque)
#ChangerIProuters(newiprouter)


#confirmation = input("voulez vous sauvegarder (O/N)?")
#if confirmation == "o":
#ActualiserFichier (fichier)
