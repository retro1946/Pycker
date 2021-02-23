from tkinter import *
from tkinter.colorchooser import *

root = Tk()

def myClick():
    color = askcolor()
    myColor = Label(root, text=(color), font=("Helvetica", 16))
    myColor.pack()


root.geometry("700x400")

root.title("Pycker")

myLabel = Label(root, text="Pycker")

myLabel.pack()

Button(root, text="Enter a color", command=myClick).pack()

Line = Label(root, text="-----------------Colors-----------------")

Line.pack()

root.mainloop()
