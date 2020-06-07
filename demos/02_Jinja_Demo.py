from flask import Flask # Web framework, stellt alle FUnktionalitäten zur Verfügung 
from flask import render_template # um html aus dem Jinja generieren zu können
from flask import request #für die Datenübertragungen (get, post) hier erhält man zum variablen Namen den Wert dazu
import json #damit man aus einem string ein array machen kann, json = Austausch von Daten
import re #regualar expressions, um buchstaben raus zu filtern, die nicht benötigt werden

app = Flask("Sternzeichen")

"""feuer, erde, luft, wasser = variable und darin wird die jeweilige Liste (inkl. Elemente Widder, Löwe etc) gespeichert """
liFeuer = ["Widder", "Löwe", "Schütze"]
liErde = ["Stier", "Jungfrau", "Steinbock"]
liLuft = ["Zwilling", "Waage", "Wassermann"]
liWasser = ["Skorpion", "Fisch", "Krebs"]
#oben ist eine Liste

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/sternzeichen")
def sternzeichen_seite():
    return render_template("sternzeichen.html", feuer=liFeuer, erde=liErde, luft=liLuft, wasser=liWasser)
# feuer = lifeuer etc. um es auf der htmlseite anzeigen lassen zu können

@app.route("/feuerzeichen")
def feuerzeichen():
    return render_template("feuerzeichen.html")


@app.route("/formular")
def formular():
    return render_template("formular.html")


def checkElementName(wert):
    """ 1. um alle Buchstaben welche nicht erwähnt, rausgeworfen werden, um richtiges Sternzeichen zu finden"""

    regex = re.compile('[^a-zA-ZäüöÄÜÖ]')
    return regex.sub('', wert)


# get Element from Arrays of sternzeichen

def getElement(wert):
    """2. schaut ob der Wert in der Liste vorhanden ist un dann Ausgabe des Elements (inkl. ".html")"""

    element = "none" #verweist du die none.html seite, falls nicht in der liste vorhanden

    if wert in liFeuer:
        element = "Feuer"

    if wert in liErde:
        element = "Erde"

    if wert in liLuft:
        element = "Luft"

    if wert in liWasser:
        element = "Wasser"

    return element
    # bedeutet, dass das Ergebnis von Element (feuer,wasser, luft, erde, none) zurück gegeben wird


# Wert von Monat und tag erhalten

def getSternzeichen(monat, tag):
    """Gibt Wert von gegebenen Monat und tag zurück

        Parameter: 
        monat (string): name des monats, 
        tag (int): numerischer tag

        gibt zurük: 

        string: Name des Sternzeichens || 'Sie sind zu blöd um Daten einzugeben'
        """

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
        sternzeichen = "Sie sind zu blöd, um Daten einzugeben"

    return sternzeichen


@ app.route('/element', methods=['GET'])
def element():
    #checkelementName wird aufgerufen, gibt ein Element aus, mit lower - klein + .html öffnet es die jeweilige Seite
    cleanedString = checkElementName(request.args.get('sternzeichen')) #reinigt das Wort von nicht alphabetischen Zeichen

    getElementString = getElement(cleanedString) #das passende Element in der Liste suchen

    setSiteString = getElementString.lower()+'.html' #generierung den Seitennamen

    return render_template(setSiteString) #Rückgabe der generierten element(feuer,wassser none).seite

""" POST für die Einabe von Daten und das Senden an den Server"""
@ app.route('/formular', methods=["POST"])
def test():
    if request.method == "POST":
        vorname = request.form["vorname"] #request eingebungen (siehe oben), form = formular, vorname = ist variable und im zweiten Vorname der eingegebene Name als key
        monat = request.form["monat"]
        tag = request.form["tag"]
        sternzeichen = getSternzeichen(monat, tag) #berechnung oben, für Sternzeichen
        json_as_array = []
        try:
    # file.jason öffnen und von einem string in ein dict umwandeln, um daraus zu verarbeitende Daten zu machen (Funktion von Json)
            with open('file.json', mode='r', encoding='utf-8') as open_file:
                json_as_array = json.load(open_file)

        except FileNotFoundError:
            print("Datei nicht gefunden")
        except PermissionError:
            print("Kein Zugriff auf die Datei")
        except Exception:
            print("Etwas anderes ging schief")
            # öffne file.json
            # suche Menschen mit gleichem Sternzeichen und schreibe sie in ein dict
            #füge eine neue Form von werten das dict zu erweitern und und schreibt es in file.json
           
        with open('file.json', mode='w', encoding='utf-8') as open_file:
            newEntry = {}
            sameStarSign = [] #liste ist hier noch leer
            countData = 0
            newEntry['vorname'] = vorname
            newEntry['sternzeichen'] = sternzeichen
            newEntry['tag'] = tag
            newEntry['monat'] = monat

            for val in json_as_array: #aus der bereits bestehenden Daten wird verglichen, wer noch dasselbe Sernzeichen hat
                if val['sternzeichen'] == sternzeichen: #wenn der Wert "Sternzeichen" gleich dem Sternzeichen in dem Formular entspricht, dann
                    sameStarSign.append(val) #hier das Paket (name, tag, monat, sternzeichen) hinzufügen

            countData = len(sameStarSign) #zählt wie viel Pakete es gibt
            json_as_array.append(newEntry) #das new entry in die dict hinzufügen
            json.dump(json_as_array, open_file) #der alte Inhalt wird mit dem neuen Inhalt ersetzt
#Ergebnis der Daten werden auf der ergebnis.html seite angezeigt
        

        return render_template("ergebnis.html", vorname=vorname, monat=monat, tag=tag, sternzeichen=sternzeichen, element=getElement(sternzeichen), countData=countData, sameStarSign=sameStarSign)
#wurde über das Formular das Sternzeichen abgefragt, dann kommt man auf die seite ergebnis.html und dort werden die Variable aus dem formular geholt und die monat=, tag= etc werden ausgegeben auf ergebnis.html und über getElement ruft man mit dem Ergebnis des Sternzeichens das passende Element auf
    return render_template('formular.html') 
    #wenn keine Daten eingegeben wurden sondern einfach nur die Formularseite angezeigt wird


if __name__ == "__main__":
    app.run(debug=True, port=5000)
