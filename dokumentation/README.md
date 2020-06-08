1. Grobe Beschreibung der Projektidee:

Die Website geht um Sternzeichen.
Der Nutzer kann mit der Eingabe seines Geburtstags sein Sternzeichen und sein Element herausfinden.Zu dem kann er eine genaue Beschreibung seines Elements lesen

Mir ist noch nicht ganz klar, ob dies über ein virtueller Chat stattfindet oder einfach eine Ein- und Ausgabe ist, aber das werden wir wahrscheinlich im Laufe des Semester lernen und je nach dem werde ich mich für eine Methode entscheiden.


2. Prototy 1 des Diagramms:

![Diagramm zum Aufbau der Website](https://github.com/selmafederl/prog2/blob/master/dokumentation/diagramm_website.jpg "Diagramm 1 Website")

2.1 Notizen zum Diagramm:

Der Internet-Nutzer hat beim Öffnen der Website die Möglichkeit entweder zur Übersicht aller aufgelisteten Sternzeichen zu gelangen oder den Chat in Anspruch zu nehmen.

2.1.1. Seite Auflistung Sternzeichen:

Gibt einfach ein Überblick aller Sternzeichen, welche unterteilt sind in Elemente 

2.1.2. Chat:

Wählt man zu Beginn den Chat öffnet sich ein Chat und dort muss angegeben werden, wann man Geburtstag hat.

Das Geburtstagsdatum ist bewusst in Tag, Monat und Jahr unterteilt. Da ich dann für die Ausführung des Algorithmus für die Berechnung des richtigen Sternzeichens (auf diesen Teil wird noch genauer eingegangen, sobald ich diesen programmieren werde). Wichtig für den problemfreien Ablauf des Algorithmus ist das erneurte Abfragen einer Frage, falls die Antwort dazu nicht korrekt ist. Wird dies nicht berücksicht so wird der Algorithmus gestoppt. Auch hier ist bei der Programmierung wichtig, Gross- und Kleinschreibung zu berücksichtigen und dies für den Prozess zu verallgemeinern (bsp. .lower(), .upper()).

Wenn das Programm die Berechnung anhand der eingegebenen Daten gemacht hat, sollte ein Link auf eine Seite auftauchen, in der das Ergebnis steht.

Wiederholen oder Ende:

Daraufhin soll im Chat nochmals die Frage kommen, ob der Benutzer noch etwas wissen möchte? Antwortet er mit "Ja" kommt nochmals die Frage mit "Was willst du wissen" - hier werde ich sehr wahrscheinlich mit einer Schleife arbeiten aber auch dieser Punkt wird nochmals aufgegriffen wenn ich das ganze programmieren werde. Bei der Antwort "Nein" verabschiedet sich der Chat

3. Offene Fragen:

Ist das Erstellen eines Chats mit unserem Wissensstand möglich?
Wie wird sich das Chatfenster öffnen? Neues Fenster? Oder ist ein kleiner Chat auf der rechten Seite möglich ohne dass die Seite verlassen wird?
Wenn der Link zur Antwort (neue Seite) geöffnet wird kann der Chat mit auf die neue Seite "genommen" werden? 

4. Beantwortung der offenen Fragen:
Das Erstellen des Chat-Fensters ist im Rahmen des Unterrichts nicht möglich. Nach Absprache mit Herrn Odoni wäre das Anwenden eines Formulars sinnvoller und auch machbarer.

Weiteres Vorgehen:
- Überarbeiten des Diagramms

5. Überarbeitetes Diagramm:

![Diagramm zum Aufbau der Website](https://github.com/selmafederl/prog2/blob/master/dokumentation/Diagramm_3.jpg "Diagramm 2 Website")

6. Abfrage nach dem Geburtstag
Für die Abfrage des Geburtstags, um das richtige Sternzeichen auszugeben, wurde ein Formular erstellt, in dem der Nutzer nach seinem Namen, seinem Geburtstag und seinem Geburtsmonat gefragt wird. Gibt er die Daten richtig an, wird im das Sternzeichen angezeigt. Gibt er ein ungültiges Geburtsdatum ein bekommt er die Meldung, dass mit den angegebenen Daten kein passendes Sternzeichen gefunden werden konnte. Zu dem wird im angezeigt, welche Nutzer noch dieses Sternzeichen haben und welches Element zu diesem Sternzeichen passt

6.1. Programmierung dahinter

6.1.1. Eingabe und Berechnung
Für die Abfrage der Daten wird ein Formular genutzt, in dem über die Methode POST Daten eingegeben und an den Server geschickt werden können.
Für die Berechnung des Sternzeichens wird über def getSternzeichen eine if, elif Formel angewendet, in der die Werte von dem Monat und Tag genutzt werden, um das richtige Sternzeichen zu finden. Gibt der Nutzer etwas vollkommen (bspw. Butter) anderes ein, so erhält er die Nachricht, dass kein Sternzeichen gefunden werden konnte und hat nochmals die Möglichkeit, seine Daten einzugeben. Wenn er jedoch ausversehen eine Zahl an den Monat ranhängt (zb. Januar3), so wird über clearString der 3er aus dem Wort gelöscht und es kann normal über getSternzeichen, nach dem Wort (zb. Januar) und der eingegebenen Zahl nach dem Sternzeichen gefiltert werden. 

Beispiel:
Ist der Monat Januar und die Zahl grösser gleich 21 ODER der Monat Februar und die Zahl kleiner gleich 19, so sollte das Ergebnis Wassermann sein

In einer Json.datei werden alle Eintragungen inkl. dem daraus berechneten Sternzeichen gespeichert. Gibt ein neuer Nutzer seine Daten ein, werden die Daten in Form eines Dict gespeichert und json erkennt die bereits eingetragenen Einträge als dict und sucht Einträge mit dem selben Sternzeichen. Diese Namen werden inkl. Geburtstag dann ausgegeben + die Anzahl an Personen werden (mit der Funktion len()) angzeigt.
Nach dem neuen Eintrag wird der alte Inhalt mit json.dump() mit dem neuen Inhalt ersetzt.

Wurde das Sternzeichen erkannt so wird dieses in den Listen liFeuer, liErde, liLuft, liWasser gesucht und über getElement einem Element zugeordnet. das zugeordnete Element wird dann über def element() mit .lower() klein geschrieben und zusätzlich wird das Wort ".html" angehängt, damit das Ergebnis des Elements direkt die Element-Seite als Verklinkung anzeigt, damit der Nutzer daraufklicken kann und dann auf der Element-Seite über sein Element lesen kann.

Neben dem Element wird auf der ergbnis.html auch die Verklinung des Sternzeichens angezeigt, so dass der Nutzer auch mehr über sein Sternzeichen erfahren kann.

Zu dem ist es über die Verlinkung über den Button "Neue Abfrage" auf der ergebnis.html möglich, auf die URL des Formulars zurück zu greifen und nochmals eine Abfrage vor zu nehmen.

7. Gestaltung
Die Website wurde mit Bootstrap-Paketen im Header ausgestattet und somit die Gestaltung für die Website gemacht

