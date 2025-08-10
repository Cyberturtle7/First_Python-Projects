import Moebel

moebelliste = []

i = 0
while i < 4:
    Artikelnummer = input("Geben Sie die Artikelnummer ein:")
    Typ = input("Geben Sie den Typ (Tisch, Stuhl etc.) ein:")
    Preis = input("Geben Sie den Preis ein:")
    moebel = Moebel.Moebel(Artikelnummer,Typ,Preis)
    moebelliste.append(moebel)
    i += 2

print(moebelliste)

print("\nNun können Sie den Preis ändern.")
eingabe = int(input("Geben Sie die Artikelnummer ein:"))
eingabe1 = int(input("Geben Sie den neuen Preis ein:"))

i = 0
while i < len(moebelliste):
    if eingabe == moebelliste[i].getPreis():
        moebelliste[i].setPreis(eingabe1)
    else:
        print("Artikelnummer nicht vorhanden!")
print(moebelliste[0])
print(moebelliste[1])