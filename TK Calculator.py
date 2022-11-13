import tkinter as tk
from math import sqrt

root = tk.Tk()
root.title("TK Calculator")
root.geometry("325x325")

calc = ''

numpad = tk.Frame(root)
calcboard = tk.Label(root, text = calc, width = 20, height = 2, bg = 'white', relief = 'groove', font = 'Calbri, 20')
calcboard.grid(column = 0, row = 0)
numpad.grid(column=0, row = 1)
numframe = tk.Frame(numpad)
numframe.grid(column = 0, row = 1)
signframe = tk.Frame(numpad)
signframe.grid(column = 1, row = 1)

class NumberKey():
    def __init__(self, number):
        self.number = number

    def create(self):
        def printnum():
            global calc
            if self.number == '+/-':
                calc += '-('
            else:
                calc += str(self.number)
            calcboard.config(text = calc)
        self.button = tk.Button(numframe, text = str(self.number), command = printnum, width = 10, height = 2, bg = 'white', relief = 'groove')

    def place(self, c, r):
        self.button.grid_forget()
        self.button.grid(column = c, row = r)

    def destroy(self):
        self.button.destroy()

class SignKey():
    def __init__(self, sign):
        self.sign = sign

    def create(self):
        def printsign():
            global calc
            calc += str(self.sign)
            calcboard.config(text = calc)
        self.button = tk.Button(signframe, text = str(self.sign), command = printsign, width = 10, height = 2, bg = 'white', relief = 'groove')

    def place(self, c, r):
        self.button.grid_forget()
        self.button.grid(column = c, row = r)

    def destroy(self):
        self.button.destroy()

def backspace():
    pass

def solve():
    global calc
    calcboard.config(text = eval(calc))
    calc = ''

def square():
    global calc
    calc += str('**2')
    calcboard.config(text = calc)

def squarert():
    global calc
    calc += str('sqrt(')
    calcboard.config(text = calc)

def brac1():
    global calc
    calc += str('(')
    calcboard.config(text = calc)

def brac2():
    global calc
    calc += str(')')
    calcboard.config(text = calc)

def cleare():
    global calc
    calc = ''
    calcboard.config(text = calc)

def clear():
    global calc
    calc = ''
    calcboard.config(text = calc)
    
    

def create_numpad():
    butt1 = tk.Button(numframe, text = 'C', command = clear, width = 10, height = 2, bg = 'white', relief = 'groove')
    butt1.grid(column = 0, row = 0)
    butt1 = tk.Button(numframe, text = '(', command = brac1, width = 10, height = 2, bg = 'white', relief = 'groove')
    butt1.grid(column = 1, row = 0)
    butt1 = tk.Button(numframe, text = ')', command = brac2, width = 10, height = 2, bg = 'white', relief = 'groove')
    butt1.grid(column = 2, row = 0)
    butt1 = tk.Button(numframe, text = 'CE', command = cleare, width = 10, height = 2, bg = 'white', relief = 'groove')
    butt1.grid(column = 0, row = 1)
    butt1 = tk.Button(numframe, text = 'x**2', command = square, width = 10, height = 2, bg = 'white', relief = 'groove')
    butt1.grid(column = 1, row = 1)
    butt1 = tk.Button(numframe, text = 'sqrt(', command = squarert, width = 10, height = 2, bg = 'white', relief = 'groove')
    butt1.grid(column = 2, row = 1)
    
    b7 = NumberKey(7)
    b7.create()
    b7.place(0,2)
    b8 = NumberKey(8)
    b8.create()
    b8.place(1,2)
    b9 = NumberKey(9)
    b9.create()
    b9.place(2,2)
    b4 = NumberKey(4)
    b4.create()
    b4.place(0,3)
    b5 = NumberKey(5)
    b5.create()
    b5.place(1,3)
    b6 = NumberKey(6)
    b6.create()
    b6.place(2,3)
    b1 = NumberKey(1)
    b1.create()
    b1.place(0,4)
    b2 = NumberKey(2)
    b2.create()
    b2.place(1,4)
    b3 = NumberKey(3)
    b3.create()
    b3.place(2,4)
    bneg = NumberKey('+/-')
    bneg.create()
    bneg.place(0,5)
    b0 = NumberKey(0)
    b0.create()
    b0.place(1,5)
    bdot = NumberKey('.')
    bdot.create()
    bdot.place(2,5)
    back = tk.Button(signframe, text = '<-', command = None, width = 10, height = 2, bg = 'white', relief = 'groove')
    back.grid(column = 0, row = 0)
    div = SignKey('/')
    div.create()
    div.place(0,1)
    mult = SignKey('*')
    mult.create()
    mult.place(0,2)
    minus = SignKey('-')
    minus.create()
    minus.place(0,3)
    plus = SignKey('+')
    plus.create()
    plus.place(0,4)
    equal = tk.Button(signframe, text = '=', command = solve, width = 10, height = 2, bg = 'lightblue', relief = 'groove')
    equal.grid(column = 0, row = 5)

create_numpad()

root.mainloop()
