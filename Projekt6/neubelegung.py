from tkinter import *
from patient import *

def hinzufuegen(meineApp):
    def eingabenAuswerten(eingabe1, eingabe2, eingabe3, geschlecht):
        patient = Patient(eingabe1.get(), eingabe2.get(), eingabe3.get(), geschlecht.get())
        erfolgreich = False
        i = 0
        while i < len(meineApp.belegung) and not erfolgreich:
            erfolgreich = meineApp.belegung[i].patientHinzufuegen(patient)
            i += 1

        if erfolgreich:
            ausgabe = Toplevel(neubelegung)
            ausgabe.title("Patient hinzugefügt")
            ausgabe.geometry("300x100")

            text = Label(ausgabe, text="Sie haben den Patienten erfolgreich hinzugefügt.")
            text.place(x=10, y=10)

            button = Button(ausgabe, text="OK")
            button["command"] = neubelegung.destroy
            button.place(x=100, y=50)

        else:
            ausgabe = Toplevel(neubelegung)
            ausgabe.title("Aufnahme nicht möglich")
            ausgabe.geometry("300x100")

            text = Label(ausgabe, text="Die Aufnahme ist leider nicht möglich.")
            text.place(x=10, y=10)

            button = Button(ausgabe, text="OK")
            button["command"] = neubelegung.destroy
            button.place(x=100, y=50)

    neubelegung = Toplevel()
    neubelegung.geometry("550x400")
    neubelegung.title("Neuen Patienten aufnehmen")

    ueberschrift = Label(neubelegung, text="Geben Sie die Daten des neuen Patienten ein:")
    ueberschrift.config(font=("Calibri", 14, "bold"))
    ueberschrift.place(x=50, y=10)

    text1 = Label(neubelegung, text="Patientennummer:")
    text1.place(x=100, y=100)
    eingabe1 = Entry(neubelegung, bd=2, width=22)
    eingabe1.place(x=220, y=100)

    text2 = Label(neubelegung, text="Vorname:")
    text2.place(x=100, y=140)
    eingabe2 = Entry(neubelegung, bd=2, width=22)
    eingabe2.place(x=220, y=140)

    text3 = Label(neubelegung, text="Nachname:")
    text3.place(x=100, y=180)
    eingabe3 = Entry(neubelegung, bd=2, width=22)
    eingabe3.place(x=220, y=180)

    text4 = Label(neubelegung, text="Geschlecht:")
    text4.place(x=100, y=220)

    geschlecht = StringVar()

    auswahl1 = Radiobutton(neubelegung, text="weiblich", variable=geschlecht, value="w")
    auswahl1.select()
    auswahl1.place(x=220, y=220)

    auswahl2 = Radiobutton(neubelegung, text="männlich",variable=geschlecht, value="m")
    auswahl2.place(x=220, y=240)

    button = Button(neubelegung, text="Eingabe")
    button["command"] = lambda: eingabenAuswerten(eingabe1, eingabe2, eingabe3, geschlecht)
    button.place(x=180, y=320)