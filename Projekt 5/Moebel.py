class Moebel:
    def __init__(self,Artikelnummer,Typ,Preis):
        self.__Artikelnummer = Artikelnummer
        self.__Typ = Typ
        self.__Preis = Preis

    def __str__(self):
        ausgabe = (f"Artikelnummer:{self.__Artikelnummer}\nTyp:{self.__Typ}\nPreis:{self.__Preis}")
        return ausgabe

    def __repr__(self):
        ausgabe = (f"Artikelnummer:{self.__Artikelnummer}\nTyp:{self.__Typ}\nPreis:{self.__Preis}")
        return ausgabe-

    def getArtikelnummer(self):
        return self.__Artikelnummer

    def getTyp(self):
        return self.__Typ

    def getPreis(self):
        return self.__Preis

    def setPreis(self,neuerPreis):
        self.__Preis = neuerPreis
        return self.__Preis