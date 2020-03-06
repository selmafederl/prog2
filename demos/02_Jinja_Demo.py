from flask import Flask
from flask import render_template
from flask import request
app = Flask("Hello World")


@app.route('/hello', methods=["GET", "POST"])
def hello_world():
	if request.method == "POST":
		vorname = request.form["vorname"]
		return "Hallo " + vorname
	return render_template('index.html')


@app.route("/test")
def test():
    return render_template("sternzeichen.html") #hier könnte man eine zweite Seite verlinken, um so auf die nächste Seite zu kommen

if __name__ == "__main__":
    app.run(debug=True, port=5000)
