Punkte = 0/5
print("Ein Latein-Quiz:")

print("\nEs gibt 5 Punkte zu erreichen")
Teilnehmer = input("Geben Sie hier Ihren Namen ein:")

print("\nHallo,",Teilnehmer)
print("Lass uns mit dem Quiz beginnen!")

print("\n\n1. Was heißt impedire auf Deutsch?")
print("\na) veranlassen")
print("b) hindern, verhindern")
print("c) vernachlässigen, nicht beachten")

Antwort = input("\nGeben Sie den Buchstaben für die richtige Antwort ein:")

if Antwort == "b":
    print("Sehr gut gemacht! Weiter so!")
    Punkte+=1
elif Antwort == "a":
    print("Das ist leider falsch")
elif Antwort =="c":
    print("Das ist leider falsch")
else:
    print("Ungültige Eingabe! Bitte geben Sie a, b oder c (in Kleinbuchstaben) ein!")

print("\n\n2. Wie lauten die Stammformen von sinere?")
print("\na) sino, sivi")
print("b) sineo, sinui")
print("c) sino, sini")

Antwort = input("\nGeben Sie den Buchstaben für die richtige Antwort ein:")

if Antwort == "a":
    print("Bravo!")
    Punkte+=1
elif Antwort == "b":
    print("Das ist leider falsch")
elif Antwort =="c":
    print("Das ist leider falsch")
else:
    print("Ungültige Eingabe! Bitte geben Sie a, b oder c (in Kleinbuchstaben) ein!")

print("\n\n3. Konjugiere velle!")

Lösung = input("\nGeben Sie alle Forrmen von Präsens Indikativ Aktiv hier ein "
               "(immer mit einem Komma und keine Leerzeichen):")
if Lösung == "volo,vis,vult,volumus,vultis,volunt":
    print("Starke Leistung!")
    Punkte+=3

else:
    print("schade!")

print("\nErreichte Punkte",Punkte,"von 5")
if Punkte == 5:
    print("Sehr gut! Volle Punktzahl!")
else:
    print("Das geht noch besser!")
