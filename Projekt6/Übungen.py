from tkinter import *


def inserter(num):
    eingabefeld.insert("end", num)

def deleter():
    eingabefeld.delete(0, "end")


def calculator():
    eingabe = eingabefeld.get()

    try:
        if "+" in eingabe:
            result = eval(eingabe)
        elif "-" in eingabe:
            result = eval(eingabe)
        elif "*" in eingabe:
            result = eval(eingabe)
        elif "/" in eingabe:
            result = eval(eingabe)
        else:
            result = "Invalid input"
    except Exception as e:
        result = "Error"

    eingabefeld.delete(0, "end")  # Clear the entry field
    eingabefeld.insert("end", str(result))  # Insert the result into the entry field

def anotherinserter():
    eingabefeld.insert(0, "-")

root = Tk()
root.title("Taschenrechner")
root.geometry("400x440+800+200")

rahmen1 = Frame(bg="#1C1C1C",height=10000, width= 10000)
rahmen1.pack()

eingabefeld = Entry(width=58,bd=2)
eingabefeld.place(x=20, y=20)

button1 = Button(text="7", height=1, width=4)
button1["command"] = lambda: inserter(7)
button1.config(font=("Arial", 20, "bold"))
button1.place(x=20, y=80)

button2 = Button(text="8", height=1, width=4)
button2["command"] = lambda: inserter(8)
button2.config(font=("Arial", 20, "bold"))
button2.place(x=112, y=80)

button3 = Button(text="9", height=1, width=4)
button3["command"] = lambda: inserter(9)
button3.config(font=("Arial", 20, "bold"))
button3.place(x=204, y=80)

button4 = Button(text="/", height=1, width=4)
button4["command"] = lambda: inserter("/")
button4.config(font=("Arial", 20, "bold"))
button4.place(x=296, y=80)

button5 = Button(text="4", height=1, width=4)
button5["command"] = lambda: inserter(4)
button5.config(font=("Arial", 20, "bold"))
button5.place(x=20, y=150)

button6 = Button(text="5", height=1, width=4)
button6["command"] = lambda: inserter(5)
button6.config(font=("Arial", 20, "bold"))
button6.place(x=112, y=150)

button7 = Button(text="6", height=1, width=4)
button7["command"] = lambda: inserter(6)
button7.config(font=("Arial", 20, "bold"))
button7.place(x=204, y=150)

button8 = Button(text="*", height=1, width=4)
button8["command"] = lambda: inserter("*")
button8.config(font=("Arial", 20, "bold"))
button8.place(x=296, y=150)

button9 = Button(text="1", height=1, width=4)
button9["command"] = lambda: inserter(1)
button9.config(font=("Arial", 20, "bold"))
button9.place(x=20, y=220)

button10 = Button(text="2", height=1, width=4)
button10["command"] = lambda: inserter(2)
button10.config(font=("Arial", 20, "bold"))
button10.place(x=112, y=220)

button11 = Button(text="3", height=1, width=4)
button11["command"] = lambda: inserter(3)
button11.config(font=("Arial", 20, "bold"))
button11.place(x=204, y=220)

button12 = Button(text="+", height=1, width=4)
button12["command"] = lambda: inserter("+")
button12.config(font=("Arial", 20, "bold"))
button12.place(x=296, y=220)

button13 = Button(text="+/-", height=1, width=4)
button13.config(font=("Arial", 20, "bold"))
button13["command"] = anotherinserter
button13.place(x=20, y=290)

button14 = Button(text="0", height=1, width=4)
button14["command"] = lambda: inserter(0)
button14.config(font=("Arial", 20, "bold"))
button14.place(x=112, y=290)

button15 = Button(text=".", height=1, width=4)
button15["command"] = lambda: inserter(".")
button15.config(font=("Arial", 20, "bold"))
button15.place(x=204, y=290)

button16 = Button(text="-", height=1, width=4)
button16["command"] = lambda: inserter("-")
button16.config(font=("Arial", 20, "bold"))
button16.place(x=296, y=290)

button17 = Button(text="=", height=1, width=15)
button17.config(font=("Arial", 20, "bold"))
button17.place(x=20, y=360)
button17["command"] = calculator

button18 = Button(text="C", height=1, width=4)
button18["command"] = deleter
button18.config(font=("Arial", 20, "bold"))
button18.place(x=296, y=360)

root.mainloop()