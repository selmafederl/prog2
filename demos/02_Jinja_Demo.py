from flask import Flask
from flask import render_template
from flask import request
app = Flask("Hello World")

@app.route('/hello')
def hello_world():
	return render_template('index.html')

@app.route("/test")
def sternzeichen_seite():
    return render_template("sternzeichen.html") #hier könnte man eine zweite Seite verlinken, um so auf die nächste Seite zu kommen

@app.route("/formular")
def formular():
    return render_template("formular.html")

@app.route('/formular', methods=["GET", "POST"])
def test():
	if request.method == "POST":
		vorname = request.form["vorname"]
		return "Hallo " + vorname
	return render_template('formular.html')
#

if __name__ == "__main__":
    app.run(debug=True, port=5000)
