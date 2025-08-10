def NotizErstellen():
    index = int(input("Geben Sie die Notiznummer ein:"))
    bezeichnung = input("Geben Sie eine Bezeichnung ein:")
    inhalt = input("Geben Sie den Inhalt der Notiz ein:")
    notiz = (index, bezeichnung, inhalt)
    notizen.append(notiz)

def NotizAnzeigen():
    eingegebeneNummer = int(input("Geben Sie die Nummer der Notiz an, die Sie sehen wollen:"))
    for notiz in notizen:
        if notiz[0] == eingegebeneNummer:
            print(notiz)
        else:
            print("Nicht vorhanden!")

def NotizLoeschen():
    eingegebeneNummer = int(input("Geben Sie die Nummer der Notiz an, die Sie löschen wollen:"))
    for notiz in notizen:
        if notiz[0] == eingegebeneNummer:
            notizen.remove(notiz)

def Speichern():
    with open("notizen.txt", "w") as f:
        for notiz in notizen:
            f.write(str(notiz[0]) + "\n")
            f.write(notiz[1] + "\n")
            f.write(notiz[2] + "\n")
            f.write("\n")

notizen = []
with open("notizen.txt", "r") as f:
    inhalt = f.readlines()
    i = 0
    while i < len(inhalt):
        index = int(inhalt[i].strip())
        bezeichnung = inhalt[i + 1].strip()
        inhalt_notiz = inhalt[i + 2].strip()
        i += 4
        notiz = (index, bezeichnung, inhalt_notiz)
        notizen.append(notiz)

while True:
    print("1. Notiz erstellen")
    print("2. Notiz anzeigen")
    print("3. Notiz löschen")
    print("4. Speichern und beenden")
    eingabe = int(input("Geben Sie Ihre Auswahl ein:"))
    print()
    if eingabe == 1:
        NotizErstellen()
    elif eingabe == 2:
        NotizAnzeigen()
    elif eingabe == 3:
        NotizLoeschen()
    elif eingabe == 4:
        Speichern()
        break

print("Tschüss!")