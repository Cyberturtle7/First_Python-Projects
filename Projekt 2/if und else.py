print("Für meine Notenverbesserung")

print("Schnitt unter 2,00 zu bekommen")
Mathe = int(input("Mathe:"))
Deutsch = int(input("Deutsch:"))
Englisch = int(input("Englisch:"))
Latein = int(input("Latein:"))
Physik = int(input("Physik:"))
Chemie = int(input("Chemie:"))

Zwischenergebnis = Mathe + Deutsch + Englisch + Latein + Physik + Chemie

if Zwischenergebnis / 6 > 2:
    print(Zwischenergebnis / 6,"Mehr lernen, noich!")
elif Zwischenergebnis / 6 <= 2:
    print(Zwischenergebnis / 6,"Gut! Weiter so!")


kapazität = 1000
bestand = 800
verfügbar=7
lieferung = int(input("Welchen Umfang hat die Warenlieferung?"))
benötigt = int(input("Wie viele Mitarbeiter benötigen Sie?"))
if bestand + lieferung <= kapazität and verfügbar >= benötigt:
    print("Die Waren können geliefert werden.")
    bestand+=lieferung
    verfügbar-=benötigt
else:
    print("Warenannahme nicht möglich!")

kapazität = 1000
bestand = 800
lieferung = int(input("Welchen Umfang hat die Warenlieferung?"))
if not bestand + lieferung > kapazität:
    print("Die Waren können geliefert werden.")
else:
    print("Die Waren können geliefert werden.")
    bestand+=lieferung


loesung = input("Bist du schlau?")
if loesung == "Ja":
    print("Das ist falsch. Versuche nochmal!")
if loesung == "Nein":
    print("Das ist richtig! Du hast es eingesehen!")

else:
    print("Ups! Irgendetwas ist schiefgelaufen! Mit Ja oder Nein beantworten!")

