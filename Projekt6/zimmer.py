class Zimmer:
    def __init__(self,nummer,betten):
        self.zimmernummer = nummer
        self.bettenzahl = betten
        self.belegung = []
        self.geschlecht = 'nicht definiert'

    def patientHinzufuegen(self,patient):
        if len(self.belegung) < self.bettenzahl:
            if self.geschlecht == patient.geschlecht:
                self.belegung.append(patient)
                erfolgreich = True
            elif self.geschlecht == 'nicht definiert':
                self.belegung.append(patient)
                self.geschlecht = patient.geschlecht
                erfolgreich = True
            else:
                erfolgreich = False
        else:
            erfolgreich = False
        return erfolgreich

    def patientEntlassen(self,patNr):
        erfolgreich = False
        i = 0
        while i < len(self.belegung):
            if self.belegung[i].patientennummer == patNr:
                self.belegung.pop(i)
                erfolgreich = True
                if len(self.belegung) == 0:
                    self.geschlecht = 'nicht definiert'
                break
            i += 1
        return erfolgreich