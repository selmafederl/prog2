1. Grobe Beschreibung der Projektidee:

Die Website geht um Sternzeichen.
Der Nutzer kann entscheiden, ob er entweder sein Geburtsdatum und Geschlecht angeben möchte, um mehr über sein Sternzeichen zu erfahren. Oder er kann auswählen, was er und sein Partner für ein Sternzeichen sind (oder Geburtsdatum), um Ergebnisse zu erhalten, ob diese zusammenpassen. Evtl. gibt es auch eine Auswahlmöglichkeit, sein Sternzeichen einzugeben und das dazugehörige chinesische Tierkreiszeichen zu erhalten.

Mir ist noch nicht ganz klar, ob dies über ein virtueller Chat stattfindet oder einfach eine Ein- und Ausgabe ist, aber das werden wir wahrscheinlich im Laufe des Semester lernen und je nach dem werde ich mich für eine Methode entscheiden.


2. Diagramm dazu:

![Diagramm zum Aufbau der Website](https://github.com/selmafederl/prog2/blob/master/diagramm_website.jpg "Bildtitel")

2.1 Noitzen zum Diagramm:

Der Internetz-Nutzer hat beim Öffnen der Website die Möglichkeit entweder zur Übersicht aller aufgelisteten Sternzeichen zu gelangen oder den Chat in Anspruch zu nehmen.

2.1.1. Seite Auflistung Sternzeichen:
Gibt einfach ein Überblick aller Sternzeichen, welche auf der Website "hinterlegt" sind. Um trotzdem auch noch zu dem Chat zu gelangen, gibt es auf der Seite noch die Möglichkeit den Chat in Anspruch zu nehmen.

2.1.2. Chat:
Wählt man zu Beginn den Chat öffnet sich ein Chat und dort muss angegeben werden, wann man Geburtstag hat.

Das Geburtstagsdatum ist bewusst in Tag, Monat und Jahr unterteilt. Da ich dann für die Ausführung des Algorithmus für die Berechnung des richtigen Sternzeichens (auf diesen Teil wird noch genauer eingegangen, sobald ich diesen programmieren werde). Wichtig für den problemfreien Ablauf des Algorithmus ist das erneurte Abfragen einer Frage, falls die Antwort dazu nicht korrekt ist. Wird dies nicht berücksicht so wird der Algorithmus gestoppt. 

Bei der Frage, was der Benutzer wissen will, wird dazu angegeben, dass er für die jeweilige Entscheidung entweder das Wort "Sternzeichen", "Tier" oder "Partner" eingeben muss, damit das Programm weiss, was er wissen will. Auch hier ist bei der Programmierung wichtig, Gross- und Kleinschreibung zu berücksichtigen und dies für den Prozess zu verallgemeinern (bsp. .lower(), .upper()).

Wenn das Programm die Berechnung anhand der eingegebenen Daten gemacht hat, sollte ein Link auf eine Seite auftauchen, in der das Ergebnis steht.

Wiederholen oder Ende:
Daraufhin soll im Chat nochmals die Frage kommen, ob der Benutzer noch etwas wissen möchte? Antwortet er mit "Ja" kommt nochmals die Frage mit "Was willst du wissen" - hier werde ich sehr wahrscheinlich mit einer Schleife arbeiten aber auch dieser Punkt wird nochmals aufgegriffen wenn ich das ganze programmieren werde. Bei der Antwort "Nein" verabschiedet sich der Chat und die Seite mit der Auflistung der Sternzeichen öffnet sich. (Somit hat der Benutzer immer noch die Möglichkeit, den Chat ein weiteres Mal aufzurufen)

3. Offene Fragen:
Ist das Erstellen eines Chats mit unserem Wissensstand möglich?
Wie wird sich das Chatfenster öffnen? Neues Fenster? Oder ist ein kleiner Chat auf der rechten Seite möglich ohne dass die Seite verlassen wird?
Wenn der Link zur Antwort (neue Seite) geöffnet wird kann der Chat mit auf die neue Seite "genommen" werden? 

