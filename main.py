from tkinter import *
import tkinter
import classic_option as cl1
import classic_option_without_rf as cl2
import compound_option as com1
import compound_option_without_rf as com2


def calcs():
    strike = Entry.get(E1)
    strike_compound = Entry.get(E2)
    maturity = Entry.get(E3)
    maturity_compound = Entry.get(E4)
    volatility = Entry.get(E5)
    option_type = Entry.get(E6)
    aux = Entry.get(E7)
    r = Entry.get(E8)
    mu = Entry.get(E9)
    s0 = Entry.get(E10)
    N = Entry.get(E11)

    strike = float(strike)
    strike_compound = float(strike_compound)
    maturity = int(maturity)
    maturity_compound = int(maturity_compound)
    volatility = float(volatility)
    option_type = str(option_type)
    aux = bool(aux)
    r = float(r)
    mu = float(mu)
    s0 = float(s0)
    N = int(N)

    if (r == 0) | (mu != 0):
        price_classic = cl2.euro_options(option_type, aux, s0, strike, maturity, mu, volatility, N)
        price_compound = com2.compound_euro_options(option_type, aux, s0, strike, strike_compound, maturity,
                                                    maturity_compound, mu, volatility, N)
    if (r != 0) | (mu == 0):
        price_classic = cl1.euro_options_risk_free(option_type, aux, s0, strike, maturity, r, volatility, N)
        price_compound = com1.compound_euro_options(option_type, aux, s0, strike, strike_compound, maturity,
                                                    maturity_compound, r, volatility, N)

    Entry.insert(E12, 0, price_classic)
    Entry.insert(E13, 0, price_compound)
    print(price_classic)
    print(price_compound)


top = tkinter.Tk()
L1 = Label(top, text="European Option pricer", ).grid(row=0, column=1)
L2 = Label(top, text="Strike Price classic", ).grid(row=1, column=0)
L3 = Label(top, text="Strike Price compound", ).grid(row=2, column=0)
L4 = Label(top, text="Maturity Date Classic", ).grid(row=3, column=0)
L5 = Label(top, text="Maturity Date compound", ).grid(row=4, column=0)
L6 = Label(top, text="Volatility of Underlying", ).grid(row=5, column=0)
L7 = Label(top, text="Option type (Call or Put)", ).grid(row=6, column=0)
L8 = Label(top, text="Aux (True/max or False/min)", ).grid(row=7, column=0)
L9 = Label(top, text="Risk-free rate", ).grid(row=8, column=0)
L10 = Label(top, text="mean of underlying").grid(row=9, column=0)
L11 = Label(top, text="Current price of underlying").grid(row=10, column=0)
L12 = Label(top, text="N of itretions").grid(row=11, column=0)
L13 = Label(top, text="Result Classic", ).grid(row=12, column=0)
L14 = Label(top, text="Result Compound", ).grid(row=13, column=0)

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
E10 = Entry(top, bd=5)
E10.grid(row=10, column=1)
E11 = Entry(top, bd=5)
E11.grid(row=11, column=1)
E12 = Entry(top, bd=5)
E12.grid(row=12, column=1)
E13 = Entry(top, bd=5)
E13.grid(row=13, column=1)

B = Button(top, text="Submit", command=calcs().grid(row=14, column=1, ))

top.mainloop()
