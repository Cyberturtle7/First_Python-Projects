notenliste = []
weiter = True
while weiter:
    print("\n Was möchten Sie tun?")
    print("1. Eine Note hinzufügen")
    print("2. Durchschnitt berechnen")
    print("3. Alle Noten ausgeben")
    print("4. Programm beenden")

    eingabe = int(input("\nGeben Sie hier Ihre Auswahl (1, 2, 3 oder 4) ein:"))

    if eingabe == 1:
        note = int(input("Geben Sie hier die Note ein:"))
        notenliste.append(note)
    elif eingabe == 2:
        summe = 0
        j = 0
        for note in notenliste:
            summe += note
            j += 1
        print("Der Durchschnittswert ist", summe / j)
    elif eingabe == 3:
        print(notenliste)
    elif eingabe == 4:
        weiter = False
print("Ich hoffe, Ich konnte helfen")

































weiter = True
notenliste = []
while weiter:
    print("\n\nWas möchten Sie tun?\n")
    print("1. Eine Note hinzufügen")
    print("2. Durchschnitt berechnen")
    print("3. Alle Noten ausgeben")
    print("4. Programm beenden\n")
    eingabe = int(input("Ihre Auswahl (1, 2, 3 oder 4): "))

    if eingabe == 1:
        note = int(input("Geben Sie die Note ein:"))
        notenliste.append(note)
    elif eingabe == 2:
        i = 0
        summe = 0
        for note in notenliste:
            summe += note
            i += 1
        if i !=0:
            print("Die Durchschnittsnote beträgt",summe / i)
        else:
            print("Noch keine Noten vorhanden.")
    elif eingabe == 3:
        print("Noten:",notenliste)
    elif eingabe == 4:
        weiter = False
        print("Auf Wiedersehen!")
    else:
        print("Ungültige Eingabe!")

notenliste = []
while True:
    print("\n\nWas möchten Sie tun?\n")
    print("1. Eine Note hinzufügen")
    print("2. Durchschnitt berechnen")
    print("3. Alle Noten ausgeben")
    print("4. Programm beenden\n")
    eingabe = int(input("Ihre Auswahl (1, 2, 3 oder 4): "))

    if eingabe == 1:
        note = int(input("Geben Sie die Note ein:"))
        notenliste.append(note)
    elif eingabe == 2:
        i = 0
        summe = 0
        for note in notenliste:
            summe += note
            i += 1
        if i !=0:
            print("Die Durchschnittsnote beträgt",summe / i)
        else:
            print("Noch keine Noten vorhanden.")
    elif eingabe == 3:
        print("Noten:",notenliste)
    elif eingabe == 4:
        break
    else:
        print("Ungültige Eingabe!")
print("Auf Wiedersehen!")