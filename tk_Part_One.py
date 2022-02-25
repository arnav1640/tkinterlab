from tkinter import *

def clicked():
    print("Button Pressed")

app = Tk()
app.title("GUI Number One")
app.geometry('300x400')

button1 = Button(app, text="This is a button", command=clicked)

button1.pack(side='top')

app.mainloop()