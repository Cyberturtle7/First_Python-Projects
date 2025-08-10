from tkinter import *

def belegungAnzeigen(meineApp):
    anzeigen = Toplevel()
    anzeigen.geometry("400x400")
    anzeigen.title("Belegungsplan anzeigen")

    ueberschrift = Label(anzeigen, text="Die aktuelle Belegung:")
    ueberschrift.config(font=("Calibri", 16))
    ueberschrift.pack(pady=20)

    rahmen = Frame(anzeigen, relief="ridge", borderwidth=1)
    rahmen.pack(pady=20,padx=30)

    scollbar = Scrollbar(rahmen)

    liste = Listbox(rahmen, yscrollcommand=scollbar.set, width=50)

    for zimmer in meineApp.belegung:
        ausgabe = f"Zimmer {zimmer.zimmernummer}"
        liste.insert(END, ausgabe)
        ausgabe = f"Bettenzahl: {zimmer.bettenzahl}"
        liste.insert(END, ausgabe)
        ausgabe = f"Belegte Betten: {len(zimmer.belegung)}"
        liste.insert(END, ausgabe)
        ausgabe = f"Patienten:"
        liste.insert(END, ausgabe)
        for patient in zimmer.belegung:
            ausgabe = patient
            liste.insert(END, ausgabe)
        if len(zimmer.belegung) == 0:
            ausgabe = "Nicht belegt."
            liste.insert(END, ausgabe)
            liste.insert(END, "")

    liste.pack(side=LEFT)
    scollbar.pack(side=LEFT, fill=Y)

    button = Button(anzeigen, text="OK", command=anzeigen.destroy, width=10, height=2)
    button.config(font=("Calibri", 10))
    button.pack(pady=10)