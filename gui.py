from tkinter import *
import tkinter
# import tkMessageBox


def proces():
    number1 = Entry.get(E1)
    number2 = Entry.get(E2)
    operator = Entry.get(E3)
    number1 = int(number1)
    number2 = int(number2)
    if operator == "+":
        answer = number1 + number2
    if operator == "-":
        answer = number1 - number2
    if operator == "*":
        answer = number1 * number2
    if operator == "/":
        answer = number1 / number2
    Entry.insert(E4, 0, answer)
    print(answer)


top = tkinter.Tk()
L1 = Label(top, text="European Option pricer", ).grid(row=0, column=1)
L2 = Label(top, text="Strike Price", ).grid(row=1, column=0)
L3 = Label(top, text="Current price", ).grid(row=2, column=0)
L4 = Label(top, text="Trade date", ).grid(row=3, column=0)
L5 = Label(top, text="Value date", ).grid(row=4, column=0)
L6 = Label(top, text="Implied volatility", ).grid(row=5, column=0)
L7 = Label(top, text="Option type (Call or Put)", ).grid(row=6, column=0)
L8 = Label(top, text="Aux (True/max or False/min)", ).grid(row=7, column=0)
L9 = Label(top, text="Option type (classic(True) or compound(False))", ).grid(row=8, column=0)
L10 = Label(top, text="Result", ).grid(row=9, column=0)

E1 = Entry(top, bd=5)
E1.grid(row=1, column=1)
E2 = Entry(top, bd=5)
E2.grid(row=2, column=1)
E3 = Entry(top, bd=5)
E3.grid(row=3, column=1)
E4 = Entry(top, bd=5)
E4.grid(row=4, column=1)
E5 = Entry(top, bd=5)
E5.grid(row=5, column=1)
E6 = Entry(top, bd=5)
E6.grid(row=6, column=1)
E7 = Entry(top, bd=5)
E7.grid(row=7, column=1)
E8 = Entry(top, bd=5)
E8.grid(row=8, column=1)
E9 = Entry(top, bd=5)
E9.grid(row=9, column=1)

B = Button(top, text="Submit", command=proces).grid(row=11, column=1, )

# top.mainloop()
