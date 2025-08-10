import datetime

def termineEinlesen():
    termine = []
    with open("termine.txt","r")as f:
        inhalt = f.readlines()
        i = 0
        while i < len(inhalt) -1:
            bezeichnung = inhalt[i]
            bezeichnung = bezeichnung[:-1]
            jahr = int(inhalt[i + 1])
            monat = int(inhalt[i + 2])
            tag = int(inhalt[i + 3])
            stunde = int(inhalt[i + 4])
            minute = int(inhalt[i + 5])
            i += 7
            datum = datetime.datetime(jahr, monat, tag, stunde, minute)
            termine.append((datum, bezeichnung))
        return termine

def naechsterTermin(termine):
    listeBereinigen(termine)
    if len(termine) > 0:
        verbleibendeZeit = termine[0][0] - datetime.datetime.now()
        tage = verbleibendeZeit.days
        sekunden = verbleibendeZeit.seconds
        minuten = sekunden // 60
        sekunden -= minuten * 60
        stunden = minuten // 60
        minuten -= stunden * 60
        print(f"Ihr nächster Termin: {termine[0][1]}")
        print(f"Verbleibende Zeit: {tage} Tage, {stunden} Stunden"
              f", {minuten} Minuten und {sekunden} Sekunden.\n")
    else:
        print("Kein Termin vorhanden!\n")

def termineAnzeigen(termine):
    for termin in termine:
        tag = termin[0].strftime("%d")
        monat = termin[0].strftime("%m")
        jahr = termin[0].strftime("%Y")
        stunde = termin[0].strftime("%H")
        minute = termin[0].strftime("%M")
        print(f"{termin[1]}: {tag}.{monat}.{jahr}"
        f"{stunde}:{minute} Uhr")
    if len(termine) == 0:
        print("Keine Termine vorhanden!")
    print()

def terminHinzufuegen(termine):
    bezeichnung = input("Was möchten Sie erledigen?")
    jahr = int(input("Geben Sie das Jahr ein:"))
    monat = int(input("Geben Sie den Monat ein:"))
    tag = int(input("Geben Sie den Tag ein:"))
    stunden = int(input("Geben Sie die Stundenzahl der Uhrzeit ein:"))
    minuten = int(input("Geben Sie die Minutenzahl der Uhrzeit ein:"))
    termin = datetime.datetime(jahr, monat, tag, stunden, minuten)
    i = 0
    if len(termine) == 0:
        termine.append((termin, bezeichnung))
    else:
        while i < len(termine):
            if termine[i][0] > termin:
                termine.insert(i, (termin, bezeichnung))
                break
            else:
                i += 1
                if i == len(termine):
                    termine.append((termin, bezeichnung))
                    break
    print()

def listeBereinigen(termine):
    if len(termine) > 0:
        while termine[0][0] <= datetime.datetime.now():
            termine.pop(0)
            if len(termine) == 0:
                break
    print()

def termineSpeichern(termine):
    f = open("termine.txt","w")
    for termin in termine:
        f.write(termin[1] + "\n")
        f.write(termin[0].strftime("%Y") + "\n")
        f.write(termin[0].strftime("%m") + "\n")
        f.write(termin[0].strftime("%d") + "\n")
        f.write(termin[0].strftime("%H") + "\n")
        f.write(termin[0].strftime("%M") + "\n")
        f.write("\n")
    f.close()