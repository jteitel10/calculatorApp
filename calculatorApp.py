from tkinter import *

# create window object
window = Tk()
# created label to go above buttons
label = Label(window, text="Calulator App")
label.grid(row=0, columnspan=4)
# create space that will display numbers
calcSpace_value = StringVar()
calcSpace = Entry(window, textvariable=calcSpace_value)
calcSpace.grid(row=1, columnspan=4)
# create a class for each button, individually set each one

allClear = Button(window, text="AC")
allClear.grid(row=2, column=0)

posNeg = Button(window, text="+/-")
posNeg.grid(row=2, column=1)

perCent = Button(window, text="%")
perCent.grid(row=2, column=2)

divISE = Button(window, text="/")
divISE.grid(row=2, column=3)

numOne = Button(window, text='1')
numOne.grid(row=5, column=0)

numTwo = Button(window, text='2')
numTwo.grid(row=5, column=1)

numThree = Button(window, text='3')
numThree.grid(row=5, column=2)

numFour = Button(window, text='4')
numFour.grid(row=4, column=2)

numFive = Button(window, text='5')
numFive.grid(row=4, column=1)

numSix = Button(window, text='6')
numSix.grid(row=4, column=0)

numSeven = Button(window, text='7')
numSeven.grid(row=3, column=0)

numEight = Button(window, text='8')
numEight.grid(row=3, column=1)

numNine = Button(window, text='9')
numNine.grid(row=3, column=2)

divISE = Button(window, text='%')
divISE.grid(row=2, column=3)

numZero = Button(window, text='0')
numZero.grid(row=6, columnspan=2)

multIPLE = Button(window, text='x')
multIPLE.grid(row=3, column=3)

subTRAX = Button(window, text='-')
subTRAX.grid(row=4, column=3)

adDZ = Button(window, text='+')
adDZ.grid(row=5, column=3)

eqUALS = Button(window, text='=')
eqUALS.grid(row=6, column=3)

perIOD = Button(window, text=".")
perIOD.grid(row=6, column=2)
# close window
window.mainloop()
