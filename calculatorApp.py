from tkinter import *

# create window object
window = Tk()
window.title("Calculator App")

# label that may be used instead of entry window to display results
# label = Label(window, text="----")
# label.grid(row=0, columnspan=4)

# create dictionary for each button and what it's text value is
# the key is the button text value, the value is the button input value
calcMap = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7,
           8: 8, 9: 9, 0: 0, '+': '+', '-': '-', '*': '*',
           '/': '/', '%': '%', 'AC': 'AC', '.': '.', '=': '=',
           '+/-': *-1}
# use a for loop to iterate through the dict, making an instance of each as a button

# define button object


def calcButton():
    pass


# define function that takes the button value .....
# receiving an error with self.text stating that theres no self defined.
# try creating an object for each button and then try using self

def buttonValue(self):
    print('{} button pressed.'.format(self.text()))


# create space that will display numbers
calcSpace_value = StringVar()
calcSpace = Entry(window, textvariable=calcSpace_value)
calcSpace.grid(row=1, columnspan=4)
# create a class for each button, individually set each one
allClear = Button(window, text='AC', command=buttonValue)
allClear.grid(row=2, column=0)

posNeg = Button(window, text='+/-', command=buttonValue)
posNeg.grid(row=2, column=1)

perCent = Button(window, text='%', command=buttonValue)
perCent.grid(row=2, column=2)

divISE = Button(window, text='/', command=buttonValue)
divISE.grid(row=2, column=3)

numOne = Button(window, text='1', command=buttonValue)
numOne.grid(row=5, column=0)

numTwo = Button(window, text='2', command=buttonValue)
numTwo.grid(row=5, column=1)

numThree = Button(window, text='3', command=buttonValue)
numThree.grid(row=5, column=2)

numFour = Button(window, text='4', command=buttonValue)
numFour.grid(row=4, column=2)

numFive = Button(window, text='5', command=buttonValue)
numFive.grid(row=4, column=1)

numSix = Button(window, text='6', command=buttonValue)
numSix.grid(row=4, column=0)

numSeven = Button(window, text='7', command=buttonValue)
numSeven.grid(row=3, column=0)

numEight = Button(window, text='8', command=buttonValue)
numEight.grid(row=3, column=1)

numNine = Button(window, text='9', command=buttonValue)
numNine.grid(row=3, column=2)

divISE = Button(window, text='%', command=buttonValue)
divISE.grid(row=2, column=3)

numZero = Button(window, text='0', command=buttonValue)
numZero.grid(row=6, columnspan=2)

multIPLE = Button(window, text='x', command=buttonValue)
multIPLE.grid(row=3, column=3)

subTRAX = Button(window, text='-', command=buttonValue)
subTRAX.grid(row=4, column=3)

adDZ = Button(window, text='+', command=buttonValue)
adDZ.grid(row=5, column=3)

eqUALS = Button(window, text='=', command=buttonValue)
eqUALS.grid(row=6, column=3)

perIOD = Button(window, text=".", command=buttonValue)
perIOD.grid(row=6, column=2)
# close window
window.mainloop()
