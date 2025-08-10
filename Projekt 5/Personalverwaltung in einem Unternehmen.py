import funktionen

mitarbeiter = [] # Hier wird die Variable "mitarbeiter" initialisiert

while True:
    print("Welche Aufgabe wollen Sie ausführen?\n")
    print("1. Einen neuen Mitarbeiter hinzufügen")
    print("2. Einen Mitarbeiter entfernen")
    print("3. Das Gehalt eines Mitarbeiters anpassen")
    print("4. Daten eines Mitarbeiters ausgeben")
    print("5. Alle Mitarbeiter ausgeben")
    print("6. Programm beenden\n")
    auswahl = int(input("Geben Sie Ihre Auswahl (1-5) ein:"))
    print()
    if auswahl == 1:
        mitarbeiter = funktionen.mitarbeiterEinfuegen(mitarbeiter)
    elif auswahl == 2:
        mitarbeiter = funktionen.mitarbeiterLoeschen(mitarbeiter)
    elif auswahl == 3:
        mitarbeiter = funktionen.gehaltAnpassen(mitarbeiter)
    elif auswahl == 4:
        funktionen.mitarbeiterdatenAusgeben(mitarbeiter)
    elif auswahl == 5:
        print(mitarbeiter)
    elif auswahl == 6:
        break
    else:
        print("Ungültige Eingabe!")
print("Auf Wiedersehen!")