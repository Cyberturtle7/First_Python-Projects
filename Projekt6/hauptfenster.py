from tkinter import *

def hauptfenster(meineApp, root):
    root.geometry("1065x300")
    root.title("Belegungsplan")
    rahmen = Frame(root, relief="raised", borderwidth=3)
    rahmen.pack(fill=BOTH, expand=1)

    button1 = Button(rahmen, text="Belegungen\nanzeigen", width=15, height=6)
    button1.config(font=("Calibri", 16, "bold"))
    button1["command"] = meineApp.anzeigen
    button1.place(x=50, y=50)

    button2 = Button(rahmen, text="Belegung\ndurchführen", width=15, height=6)
    button2.config(font=("Calibri", 16, "bold"))
    button2["command"] = meineApp.neubelegung
    button2.place(x=430, y=50)

    button3 = Button(rahmen, text="Entlassung\nvornehmen", width=15, height=6)
    button3 .config(font=("Calibri", 16, "bold"))
    button3["command"] = meineApp.entlassung
    button3.place(x=810, y=50)