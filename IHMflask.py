from flask import Flask
import datetime
app = Flask(__name__)

@app.route("/") #Une vue
def index():
    return "Hello World!"

@app.route("/heure")
def heure():
	now = datetime.datetime.now()
	return "Heure : {}".format(now)

if __name__ == "__main__":
    app.run(host='10.160.108.106', port=80, debug=True)#mode debug a supprimer

