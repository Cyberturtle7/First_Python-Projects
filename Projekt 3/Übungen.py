for i in range(60,80,3):
    print(i)

while True:
    eingabe = int(input("16*16:"))
    if eingabe == 256:
        break
print("Richtig!")

laender = ["deutschland","frankreich","italien","polen","schweiz","oesterreich"]
print("Erster Eintrag:",laender[0])
print("Vorletzter Eintrag:",laender[-2])
eingabe = input("Geben Sie ein Land ein, dass sie aus der Liste entfernen möchten:")
laender.remove(eingabe)
print("Länge:",len(laender))