class Patient:
    def __init__(self,nummer,vorname,nachname,geschlecht):
        self.patientennummer = nummer
        self.vorname = vorname
        self.nachname = nachname
        self.geschlecht = geschlecht

    def __str__(self):
        return f'{self.patientennummer} ({self.vorname} {self.nachname})'