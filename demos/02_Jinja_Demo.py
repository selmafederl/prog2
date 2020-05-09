from flask import Flask
from flask import render_template
from flask import request
app = Flask("Hello World")


@app.route('/')
def hello_world():
    return render_template('index.html')


# @app.route("/sternzeichen")
# def sternzeichen_seite():
#     # hier könnte man eine zweite Seite verlinken, um so auf die nächste Seite zu kommen
#     return render_template("sternzeichen.html")


@app.route("/sternzeichen")
def sternzeichen_seite():  # funktioniert irgendwie nicht.. Wieso?
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

# 21.03. - 20.04. ➔ Widder

# 21.04. - 20.05. ➔ Stier

# 21.05. - 21.06. ➔ Zwilling

# 22.06. - 22.07. ➔ Krebs

# 23.07. - 23.08. ➔ Löwe

# 24.08. - 23.09. ➔ Jungfrau

# 24.09. - 23.10. ➔ Waage

# 24.10. - 22.11. ➔ Skorpion

# 23.11. - 21.12. ➔ Schütze

# 22.12. - 20.01. ➔ Steinbock

# 21.01. - 19.02. ➔ Wassermann

# 20.02. - 20.03. ➔ Fisch
@app.route('/formular', methods=["POST"])
def test():
    if request.method == "POST":
        vorname = request.form["vorname"]
        monat = request.form["monat"]
        tag = request.form["tag"]
        sternzeichen = ""
        if monat == "Januar" and int(tag) >= 21 or monat == "Februar" and int(tag) <= 19:
            sternzeichen = "Wassermann"

        elif monat == "Februar" and int(tag) >= 20 or monat == "März" and int(tag) <= 20:
            sternzeichen = "Fisch"

        elif monat == "März" and int(tag) >= 21 or monat == "April" and int(tag) <= 20:
            sternzeichen = "Widder"

        elif monat == "April" and int(tag) >= 21 or monat == "Mai" and int(tag) <= 20:
            sternzeichen = "Stier"

        elif monat == "Mai" and int(tag) >= 21 or monat == "Juni" and int(tag) <= 21:
            sternzeichen = "Zwilling"

        elif monat == "Juni" and int(tag) >= 22 or monat == "Juli" and int(tag) <= 22:
            sternzeichen = "Krebs"

        elif monat == "Juli" and int(tag) >= 23 or monat == "August" and int(tag) <= 23:
            sternzeichen = "Löwe"

        elif monat == "Juli" and int(tag) >= 24 or monat == "September" and int(tag) <= 23:
            sternzeichen = "Jungfrau"

        elif monat == "September" and int(tag) >= 24 or monat == "Oktober" and int(tag) <= 23:
            sternzeichen = "Waage"

        elif monat == "Oktober" and int(tag) >= 24 or monat == "November" and int(tag) <= 22:
            sternzeichen = "Skorpion"

        elif monat == "November" and int(tag) >= 24 or monat == "Dezember" and int(tag) <= 22:
            sternzeichen = "Schütze"

        elif monat == "Dezember" and int(tag) >= 22 or monat == "Januar" and int(tag) <= 20:
            sternzeichen = "Steinbock"
        else:
            sternzeichen = "Sie sind zu blöd um Daten einzugeben"

        return render_template("ergebnis.html", vorname=vorname, monat=monat, tag=tag, sternzeichen=sternzeichen)
        # Hier müsste dann auch das Ergebnis des Formulars rauskommen - Sternzeichen etc aber Programmierung noch nicht so weit
    return render_template('formular.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
