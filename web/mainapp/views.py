from flask import Flask, render_template, url_for, request
from reseau import *
import os

app = Flask(__name__)

@app.route("/")
@app.route("/accueil")
def index():
    return render_template('accueil.html')
      
@app.route("/reseau", methods=['GET', 'POST'])
def reseau():
	if request.method == 'POST' and request.form['formulaire'] == 'Modifier Ethernet':
		if request.form['adIP']and request.form['masque'] and request.form['route']:
			IPstatique = request.form['adIP']
			MASQUEstatique = request.form['masque']
			Route = request.form['route']
			
			ChangerIPstatique(IPstatique, MASQUEstatique)
			ModifierServeur(IPstatique)
			ChangerIProuters(Route)
		else:
			return "unvalide"#pop-up java script erreur		
			
	elif request.method == 'POST' and request.form['formulaire'] == 'Modifier WIFI':
		if request.form['ssid'] and request.form['mdp']:
			newSSID = request.form['ssid']
			newMDP = request.form['mdp']
			
			ModifierSSID(newSSID)
			ModifierMDP(newMDP)
		else:
			return "unvalide"#pop-up java script erreur	
	elif request.method == 'POST' and request.form['formulaire'] == 'Redemarrer':
		myCmd = 'sudo reboot'
		os.system(myCmd)
		return "reboot"	
	
	ip, masque, ipdebut, ipfin = LireIpStatique()
	ipR, ipRdebut, ipRfin = LireIprouters()
	return render_template('reseau.html', ip=ip, masque=masque, ipR=ipR)
    #https://openclassrooms.com/fr/courses/1654786-creez-vos-applications-web-avec-flask/1655474-lechange-de-donnees
    
@app.route("/serveur")
def serveur():
    return render_template('serveur.html')
    
@app.route("/support")
def support():
    return render_template('support.html')

if __name__ == "__main__":
	app.run()

