import fktMailverteiler

mails = fktMailverteiler.ListeEinlesen()

print("Dieses Programm verwaltet eine Liste für einen Mailverteiler.\n")

while True:
    print("\n1. E-Mail-Adressen mit zugehörigen Namen anzeigen")
    print("2. E-Mail-Adresse mit zugehörigem Namen hinzufuegen")
    print("3. Speichern und beenden\n")
    eingabe = int(input("Was möchten Sie tun?"))

    if eingabe == 1:
        fktMailverteiler.ListeAnzeigen(mails)
    elif eingabe == 2:
        fktMailverteiler.ListeErgaenzen(mails)
    elif eingabe == 3:
        fktMailverteiler.ListeSpeichern(mails)
        break

print("Tschau mit V")
