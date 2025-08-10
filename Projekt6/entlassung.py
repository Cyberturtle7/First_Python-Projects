from tkinter import *

def entlassen(meineApp):
    def eingabenAuswerten():

        erfolgreich = False
        i = 0
        while i < len(meineApp.belegung) and not erfolgreich:
            erfolgreich = meineApp.belegung[i].\
                patientEntlassen(patNr.get())
            i += 1

        if erfolgreich:
            ausgabe = Toplevel(entlassung)
            ausgabe.title("Patient entlassen")
            ausgabe.geometry("300x100")

            text = Label(ausgabe, text="Der Patient wurde aus dem Belegungsplan entfernt.")
            text.place(x=10, y=10)

            button = Button(ausgabe, text="OK")
            button["command"] = ausgabe.destroy
            button.place(x=100, y=50)

        else:
            ausgabe = Toplevel(entlassung)
            ausgabe.title("Entlassung nicht möglich")
            ausgabe.geometry("300x100")

            text = Label(ausgabe, text="Die Patientennummer ist nicht\n"
                                             "im Belegungsplan enthalten.")
            text.place(x=10, y=10)

            button = Button(ausgabe, text="OK")
            button["command"] = ausgabe.destroy
            button.place(x=100, y=50)

    entlassung = Toplevel()
    entlassung.geometry("550x250")
    entlassung.title("Patienten entlassen")

    ueberschrift = Label(entlassung, text="Welchen Patienten möchten Sie entlassen?")
    ueberschrift.config(font=("Calibri", 14, "bold"))
    ueberschrift.place(x=50, y=10)

    text = Label(entlassung, text="Patientennummer:")
    text.place(x=100, y=100)
    patNr = Entry(entlassung, bd=2, width=22)
    patNr.place(x=220, y=100)

    button = Button(entlassung, text="Eingabe")
    button["command"] = eingabenAuswerten
    button.place(x=180, y=150)