import datetime

class Mitarbeiter:
    def __init__(self, personalnummer, nachname, vorname, geburtsdatum, gehalt):
        self.__personalnummer = personalnummer
        self.__nachname = nachname
        self.__vorname = vorname
        self.__geburtsdatum = geburtsdatum
        self.__gehalt = gehalt

    def __str__(self):
        ausgabe = f"Personalnummer: {self.__personalnummer}\n"
        ausgabe += f"Name: {self.__vorname} {self.__nachname}\n"
        ausgabe += "Geburtsdatum:"
        ausgabe += self.__geburtsdatum.strftime("%d.%m.%Y")
        ausgabe += f"Alter: {self.alterBerechnen()}\n"
        ausgabe += f"Gehalt: {self.__gehalt}\n"
        return ausgabe

    def __repr__(self):
        ausgabe = (f"{self.__personalnummer}: {self.__vorname}")
        ausgabe += (f"{self.__nachname}")
        return ausgabe

    def getPersonalnummer(self):
        return self.__personalnummer

    def setGehalt(self, gehalt):
        self.__gehalt = gehalt

    def alterBerechnen(self):
        heute = datetime.date.today()
        if ((heute.month, heute.day) < (self.__geburtsdatum.month, self.__geburtsdatum.day)):
            return heute.year - self.__geburtsdatum.year - 1
        else:
            return heute.year - self.__geburtsdatum.year