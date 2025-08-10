import Mitarbeiter
import datetime

def mitarbeiterEinfuegen(mitarbeiterliste):
    personalnummer = int(input("Personalnummer:"))
    nachname = input("Nachname:")
    vorname = input("Vorname:")
    geburtstag = input("Geburtsdatum (tt.mm.jjjj):")
    if geburtstag[0] == "0":
        tag = int(geburtstag[1])
    else:
        tag = int(geburtstag[:2])
    if geburtstag[3] == "0":
        monat = int(geburtstag[4])
    else:
        monat = int(geburtstag[3:5])
    jahr = int(geburtstag[6:])
    datum = datetime.date(jahr, monat, tag)
    gehalt = int(input("Gehalt:"))
    mitarbeiter = Mitarbeiter.Mitarbeiter(personalnummer, nachname, vorname, datum, gehalt)
    mitarbeiterliste.append(mitarbeiter)
    return mitarbeiterliste

def mitarbeiterLoeschen(mitarbeiterliste):
    nummer = int(input("Geben Sie die Personalnummer des Mitarbeiters ein:"))
    gefunden = False
    i = 0
    while i < len(mitarbeiterliste):
        if nummer == mitarbeiterliste[i].getPersonalnummer():
            del mitarbeiterliste[i]
            gefunden = True
        i += 1
    if gefunden:
        print(f"Mitarbeiter {nummer} wurde gelöscht.")
    else:
        print("Personalnummer nicht vorhanden.")
    return mitarbeiterliste

def gehaltAnpassen(mitarbeiterliste):
    nummer = int(input("Geben Sie die Personalnummer des Mitarbeiters ein:"))
    neuesGehalt = int(input("Geben Sie das neue Gehalt ein:"))
    gefunden = False
    i = 0
    while i < len(mitarbeiterliste):
        if nummer == mitarbeiterliste[i].getPersonalnummer():
            mitarbeiterliste[i].setGehalt(neuesGehalt)
            gefunden = True
        i += 1
    if gefunden:
        print(f"Gehalt von Mitarbeiter{nummer} wurde angepasst.")
    else:
        print("Personalnummer nicht vorhanden.")
    return mitarbeiterliste

def mitarbeiterdatenAusgeben(mitarbeiterliste):
    nummer = int(input("Geben Sie die Personalnummer des Mitarbeiters ein:"))
    gefunden = False
    for mitarbeiter in mitarbeiterliste:
        if mitarbeiter.getPersonalnummer() == nummer:
            print(mitarbeiter)
            gefunden = True
    if not gefunden:
        print("Personalnummer nicht vorhanden.")