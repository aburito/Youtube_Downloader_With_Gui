from tkinter import *

top = Tk()
top.geometry("700x300")
top.title("StringVar Object in Entry Widget")

var = StringVar(top)

def submit():
   Label2.config(text="Your User ID is: " +var.get(), font=("Calibri,15,Bold"))

Label1 = Label(top, text='Your User ID:')
Label1.grid(column=0, row=0, padx=(20,20), pady=(20,20))

myEntry = Entry(top, textvariable=var)
myEntry.grid(column=1, row=0, padx=(20,20), pady=(20,20))

myButton = Button(top, text="Submit", command=submit)
myButton.grid(column=2, row=0)

Label2 = Label(top, font="Calibri,10")
Label2.grid(column=0, row=1, columnspan=3)

top.mainloop()