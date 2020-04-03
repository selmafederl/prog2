from flask import Flask
from flask import render_template
from flask import request
app = Flask("Hello World")

@app.route('/hello')
def hello_world():
    return render_template('index.html')

@app.route("/sternzeichen")
def sternzeichen_seite():
     return render_template("sternzeichen.html") #hier könnte man eine zweite Seite verlinken, um so auf die nächste Seite zu kommen

@app.route("/sternzeichen1")
def jinja1(): #funktioniert irgendwie nicht.. Wieso?
    feuer = ["Widder", "Löwe", "Schütze"]
    erde = ["Stier", "Jungfrau", "Steinbock"]
    luft = ["Zwilling", "Waage", "Wassermann"]
    wasser = ["Skorpion", "Fisch", "Krebs"]
    return render_template("sternzeichen.html", feuer=feuer, erde=erde, luft=luft, wasser=wasser)

@app.route("/feuerzeichen")
def feuerzeichen():
    return render_template("feuerzeichen.html")

@app.route("/formular")
def formular():
    return render_template("formular.html")

@app.route('/formular', methods=["GET", "POST"])
def test():
    if request.method == "POST":
        vorname = request.form["vorname"]
        return "Hallo " + vorname
        #Hier müsste dann auch das Ergebnis des Formulars rauskommen - Sternzeichen etc
    return render_template('formular.html')



if __name__ == "__main__":
    app.run(debug=True, port=5000)
