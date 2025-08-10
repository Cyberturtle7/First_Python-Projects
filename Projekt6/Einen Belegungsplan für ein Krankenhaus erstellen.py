from hauptfenster import *
from anzeigen import *
from neubelegung import *
from entlassung import *
from zimmer import *

class App:

    def __init__(self):
        self.belegung = [Zimmer(101, 4)]
        self.belegung.append(Zimmer(102, 4))
        self.belegung.append(Zimmer(201, 2))
        self.belegung.append(Zimmer(202, 3))

    def hauptfenster(self, root):
        hauptfenster(self, root)

    def anzeigen(self):
        belegungAnzeigen(self)

    def neubelegung(self):
        hinzufuegen(self)

    def entlassung(self):
        entlassen(self)

root = Tk()
meineApp = App()
meineApp.hauptfenster(root)
root.mainloop()