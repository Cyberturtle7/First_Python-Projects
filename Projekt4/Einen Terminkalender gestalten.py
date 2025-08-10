import funktionen

termine = funktionen.termineEinlesen()
funktionen.naechsterTermin(termine)
while True:
    print("Programmfunktionen\n")
    print("1. Alle Termine ausgeben")
    print("2. Nächsten Termin anzeigen")
    print("3. Termin hinzufügen")
    print("4. Vergangene Termine aus der Liste löschen")
    print("5. Programm speichern und beenden\n")
    eingabe = int(input("Ihre Auswahl: "))
    if eingabe == 1:
        funktionen.termineAnzeigen(termine)
    elif eingabe == 2:
        funktionen.naechsterTermin(termine)
    elif eingabe == 3:
        funktionen.terminHinzufuegen(termine)
    elif eingabe == 4:
        funktionen.listeBereinigen(termine)
    elif eingabe == 5:
        funktionen.termineSpeichern(termine)
        break
    else:
        print("Ungültige Eingabe!")