from tkinter import *
from tkinter import colorchooser

root = Tk()

# Create Title
root.title("New Windows Creation")
root.geometry("300x300")

def color():
	my_color = colorchooser.askcolor()[1]
	l1 = Label(root, text = my_color).pack()
	l2 = Label(root, text = "You Picked a color!!", bg = my_color).pack()
b1 = Button(root, text = "Pick color", command = color).pack()


root.mainloop()