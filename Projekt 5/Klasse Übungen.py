class Kunden:
    def __init__(self, vorname, nachname):
        self.vorname = vorname
        self.nachname = nachname
        self.bestellungen = []

    def __str__(self):
        ausgabe = self.vorname + " " + self.nachname
        ausgabe += " " + str(self.bestellungen)
        return ausgabe

    def __repr__(self):
        ausgabe = (f"{self.vorname} {self.nachname}")
        return ausgabe


kunde1 = Kunden("Michael", "Bayer")
kunde2 = Kunden("Nina","Hauser")

kundenliste = [kunde1, kunde2]

print(kundenliste)