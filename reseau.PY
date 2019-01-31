#fichier = open("/etc/dhcpcd.conf", "r")

#Configuration statique
def LireIpStatique() :
	fichierR = open("dhcptest.conf", "r")
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

def ChangerIPstatique():
	fichierR = open("dhcptest.conf", "r")
	contenu = fichierR.read()

	ip, masque, ipdebut, ipfin = LireIpStatique()
	newip = input("ip :") #modifier par la new ip de l'utilisateur
	newip += "/" + input("masque :") #modifier par la new masque de l'utilisateur
	ip = ip + "/" + masque
	contenu = contenu.replace(ip, newip)

	fichierR.close()
	fichierW = open("dhcptest.conf", "w")
	fichierW.write(contenu)
	fichierW.close()

def LireIprouters() :
	fichierR = open("dhcptest.conf", "r")
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

def ChangerIProuters():
	fichierR = open("dhcptest.conf", "r")
	contenu = fichierR.read()

	ip, ipdebut, ipfin = LireIprouters()
	newip = input("ip :") #modifier par la new ip de l'utilisateur
	contenu = contenu.replace(ip, newip)

	fichierR.close()
	fichierW = open("dhcptest.conf", "w")
	fichierW.write(contenu)
	fichierW.close()


#Configuration dynamique

#ip, masque, ipdebut, ipfin = LireIpStatique(contenu)
#print ("Votre adresse ip :",ip,"Masque :",masque)
ChangerIProuters()


#confirmation = input("voulez vous sauvegarder (O/N)?")
#if confirmation == "o":
#ActualiserFichier (fichier)