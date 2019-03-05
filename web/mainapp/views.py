from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/accueil")
def index():
    return render_template('accueil.html')
    
@app.route("/reseau", methods=['GET', 'POST'])
def reseau():
    return render_template('reseau.html')
    #https://openclassrooms.com/fr/courses/1654786-creez-vos-applications-web-avec-flask/1655474-lechange-de-donnees
    
@app.route("/serveur")
def serveur():
    return render_template('serveur.html')
    
@app.route("/support")
def support():
    return render_template('support.html')

if __name__ == "__main__":
    app.run()

