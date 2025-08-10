print("Dieses Programm ist für Ihre Terminverwaltung zuständig")
def TermineAnzeigen(termine):
    print(termine)
    return termine
def TermineHinzufügen(termin):
    termin.append(termin)
while True:
print ("Was möchten Sie tun?")
print("1. Alle Termine anzeigen lassen.")
print("1")
eingabe = int(input("Geben Sie Ihre Auswahl ein:"))
if eingabe == 1:
    TermineAnzeigen(termine)
if eingabe == 2:
    termin = 0
    TermineHinzufügen(termin)