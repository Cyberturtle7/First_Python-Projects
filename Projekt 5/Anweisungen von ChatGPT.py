class Schueler:
    def __init__(self,vorname,nachname,alter,klassenstufe,durchschnittsnote):
        self.__vorname = vorname
        self.__nachname = nachname
        self.__alter = alter
        self.__klassenstufe = klassenstufe
        self.__durchschnittsnote = durchschnittsnote

    def NoteAktualisieren(self,note):
        self.__durchschnittsnote = (self.__durchschnittsnote + note)/2

    def SchuelerAttributeAusgeben(self):
        print(f"Vorname: {self.__vorname} \nNachname: {self.__nachname} \nAlter: {self.__alter} \n"
              f"Klassenstufe: {self.__klassenstufe} \nDurchschnittsnote: {self.__durchschnittsnote}")

schuelerliste = []
vorname = input("Vorname: ")
nachname = input("Nachname: ")
alter = input("Alter: ")
klassenstufe = input("Klassenstufe: ")
durchschnittsnote = input("Durchschnittsnote: ")
schueler = (vorname,nachname,alter,klassenstufe,durchschnittsnote)
schuelerliste.append(schueler)


class Auto:
    def __init__(self,marke,modell,farbe,geschwindigkeit):
        self.__marke = marke
        self.__modell = modell
        self.__farbe = farbe
        self.__geschwindigkeit = geschwindigkeit

    def GeschwindigkeitErhoehen(self):
        zusatzgeschwindigkeit = int(input("Um wie viel km/h möchten Sie beschleunigen:"))
        endgeschwindigkeit0 = self.__geschwindigkeit + zusatzgeschwindigkeit
        if endgeschwindigkeit0 > 200:
            anpassungswert = endgeschwindigkeit0 - 200
            endgeschwindigkeit1 = self.__geschwindigkeit + (zusatzgeschwindigkeit - anpassungswert)
            self.__geschwindigkeit = endgeschwindigkeit1
        else:
            self.__geschwindigkeit = endgeschwindigkeit0
        print(self.__geschwindigkeit)

    def GeschwindigkeitSenken(self):
        zusatzgeschwindigkeit = int(input("Um wie viel km/h möchten Sie bremsen:"))
        endgeschwindigkeit = self.__geschwindigkeit - zusatzgeschwindigkeit
        self.__geschwindigkeit = endgeschwindigkeit
        print(self.__geschwindigkeit)

    def GeschwindigkeitAnzeigen(self):
        print(f"Ihr Auto {self.__marke} ist momentan {self.__geschwindigkeit}km/h schnell.")

auto1 = Auto("Toyota","Avensis","Silber",40)
auto1.GeschwindigkeitErhoehen()
auto1.GeschwindigkeitSenken()
auto1.GeschwindigkeitAnzeigen()




class Bankkonto:
    def __init__(self,kontonummer,kontostand):
        self.__kontonummer = kontonummer
        self.__kontostand = kontostand
        int(self.__kontostand)

    def einzahlen(self):
        eingezahltesumme = int(input("Wie viel möchten Sie einzahlen:"))
        neuerkontostand = self.__kontostand + eingezahltesumme
        self.__kontostand = neuerkontostand

    def abheben(self):
        abgehobenesumme = int(input("Wie viel möchten Sie abheben:"))
        if abgehobenesumme <= self.__kontostand:
            neuerkontostand = self.__kontostand - abgehobenesumme
            self.__kontostand = neuerkontostand
        else:
            print("Fehler!")

    def kontostand_abfragen(self):
        print(self.__kontostand)

account = Bankkonto(0,0)
while True:
    eingabe = int(input("einzahlen(1),abheben(2),anzeigen(3),beenden(4)?"))
    if eingabe == 1:

        account.einzahlen()
    elif eingabe == 2:
        account.abheben()

    elif eingabe == 3:
        account.kontostand_abfragen()

    elif eingabe == 4:
        break

print("Tschüss!")





class Person:
    def __init__(self,vorname,nachname,alter):
        self.__vorname = vorname
        self.__nachname = nachname
        self.__alter = alter

    def InfoAnzeigen(self):
        print(f"{self.__vorname},{self.__nachname},Alter:{self.__alter}")


person = Person("Max","Mustermann",30)

person.InfoAnzeigen()