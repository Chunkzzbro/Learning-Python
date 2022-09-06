from tkinter import *
from turtle import width

def km_to_miles():
    print(e1_value.get())
    miles = float(e1_value.get()) * 1.6
    t1.insert(END,miles)

window = Tk()               #Making an empty window 

b1 = Button(window,text = "Execute",command = km_to_miles)         #Adding a button to the empty window
b1.grid(row = 0,column = 0)           #You can either use .pack or .grid. With grid you have more control over the location of the button to be placed

e1_value =StringVar()
e1 = Entry(window,textvariable=e1_value)                #Creating an entry in the gui where user can enter data
e1.grid(row = 0, column = 1)

t1 = Text(window,height = 1, width = 20)               #Creating a text window 
t1.grid(row = 0, column = 2) 

window.mainloop()

