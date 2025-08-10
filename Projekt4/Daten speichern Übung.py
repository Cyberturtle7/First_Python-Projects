import datetime
termine = []
i = 0
inhalt = 0

while i < len(inhalt) - 1:
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