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
	
	i = 0
	masque = ""
	while contenu[ipfin+i] != "#":
		masque += contenu[ipfin+i]
		i+=1


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

	ipRdebut = contenu.find("static routers=")
	ipRdebut += 15
	i = 0
	ipR = ""
	while contenu[ipRdebut+i] != "#": #!!!!Mettre hashtag dans le .conf!!!
		ipR += contenu[ipRdebut+i]
		i+=1
	ipRfin = ipRdebut+i+1

	fichierR.close()
	return (ipR, ipRdebut, ipRfin)

def ChangerIProuters(newiprouter):
	fichierR = open("/home/pi/ormeau/web/mainapp/dhcptest.conf", "r")
	contenu = fichierR.read()

	ip, ipdebut, ipfin = LireIprouters()
	contenu = contenu.replace(ip, newiprouter)

	fichierR.close()
	fichierW = open("/home/pi/ormeau/web/mainapp/dhcptest.conf", "w")
	fichierW.write(contenu)
	fichierW.close()
	
#---------------------------WIFI----------------------------------------	
#/etc/wpa_supplicant/wpa_supplicant.conf
#"/home/pi/ormeau/web/wpa_supplicanttest.conf"

def LireSSID ():
	fichierR = open("/etc/wpa_supplicant/wpa_supplicant.conf", "r")
	contenu = fichierR.read()

	ssiddebut = contenu.find('ssid="')
	ssiddebut += 6
	i = 0
	ssid = ""

	while contenu[ssiddebut+i] != '"':
		ssid += contenu[ssiddebut+i]
		i+=1
	ssidfin = ssiddebut+i

	fichierR.close()
	return (contenu, ssid)

def ModifierSSID(newSSID):
	contenu, ssid = LireSSID ()
	contenu = contenu.replace(ssid, newSSID)

	fichierW = open("/etc/wpa_supplicant/wpa_supplicant.conf", "w")
	fichierW.write(contenu)
	fichierW.close()

def LireMDP ():
	fichierR = open("/etc/wpa_supplicant/wpa_supplicant.conf", "r")
	contenu = fichierR.read()

	mdpdebut = contenu.find('psk="')
	mdpdebut += 5
	i = 0
	mdp = ""

	while contenu[mdpdebut+i] != '"':
		mdp += contenu[mdpdebut+i]
		i+=1
	mdpfin = mdpdebut+i

	fichierR.close()
	return (contenu, mdp)

def ModifierMDP(newMDP):
	contenu, mdp = LireMDP ()
	contenu = contenu.replace(mdp, newMDP)

	fichierW = open("/etc/wpa_supplicant/wpa_supplicant.conf", "w")
	fichierW.write(contenu)
	fichierW.close()
#------------------------IP_serveur_flask-------------------------------
def LireServeur():
	fichierR = open("/home/pi/ormeau/web/run.py", "r")
	contenu = fichierR.read()

	IPdebut = contenu.find("host='")
	IPdebut += 6
	i = 0
	IPserv = ""

	while contenu[IPdebut+i] != "'":
		IPserv += contenu[IPdebut+i]
		i+=1
	IPfin = IPdebut+i

	fichierR.close()
	return (contenu, IPserv)

def ModifierServeur(newIPserv):
	contenu, IPserv = LireServeur()
	contenu = contenu.replace(IPserv, newIPserv)

	fichierW = open("/home/pi/ormeau/web/run.py", "w")
	fichierW.write(contenu)
	fichierW.close()

#Configuration dynamique

#ip, masque, ipdebut, ipfin = LireIpStatique()
#print ("Votre adresse ip :",ip,"Masque :",masque)
#ChangerIProuters(newiprouter)

#ipR, ipRdebut, ipRfin =LireIprouters()
#print "Votre adresse ip :",ipR


#confirmation = input("voulez vous sauvegarder (O/N)?")
#if confirmation == "o":
#ActualiserFichier (fichier)
