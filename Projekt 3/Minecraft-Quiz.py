liste = ["Albert","Herbert","Norbert","Robert"]

eingabetest = input("Gib die Namen ein:")
if eingabetest == liste:
    print("Es hat geklappt!")

punkte = 0

print("Ein Minecraft-Quiz:")

name = input("\nDein Spielername:")
print("Hallo,",name,"wähle deinen Schwierigkeitsgrad")

print("\n1. Easy")
print("2. Normal")
print("3. Hard")

eingabe = input("\nGib deinen Schwierigkeitsgrad hier ein:")
if eingabe == "Easy":
    antwort1 = int(input("\nWann wurde Minecraft veröffentlicht?"))
    if antwort1 == 2011:
        print("Richtig!")
        punkte += 1
    else:
        print("Falsch!")
    antwort2 = int(input("\nWie viele Diamanten braucht man für eine Diamantenspitzhacke?"))
    if antwort2 == 3:
        print("Richtig!")
        punkte += 1
    else:
        print("falsch")
    antwort3 = int(input("\nWie viel HERZEN Schaden verursacht ein Netherite-Schwert?"))
    if antwort3 == 4:
        print("Richtig!")
        punkte += 1
    else:
        print("Falsch!")

elif eingabe == "Hard":
    antwort7 = input("\nListe alle feindlichen Kreaturen auf "
                     "(ohne Leerzeichen, nur Spawneggs, erster Buchstabe großgeschrieben, Java-Edition):")
    monsterliste = ["Zombie,Zombiedorfbewohner,Wüstenzombie,Ertrunkener,ZombifizierterPiglin,Phantom,"
                    "Skelett,Eiswanderer,Witherskelett,Creeper,Spinne,Höhlenspinne,Schleim,Wärter,Enderman,Hexe,"
                    "Wächter,GroßerWächter,Plünderer,Verwüster,Diener,Magier,Plagegeister,"
                    "Piglin,Piglin-Barbar,Hoglin,Zoglin,Ghast,Magmawürfel,Lohe,Wither,Silberfisch,Endermilbe,Shulker,Enderdrache"]
    if antwort7 == monsterliste:
        print("Richtig!")
        punkte += 1
    else:
        print("Falsch!")

if punkte == 0 or 1:
    print("\nEinen oder keinen Punkt, Minecraft-Noob!")
elif punkte == 2:
    print("\n2 Punkte, Minecraft-Pro!")
elif punkte == 3:
    print("\n Alle Punkte erreicht, Minecraft-God!")


