from tkinter import *

app = Tk()
app.title("GUI Example 5")
app.geometry('400x400')

w = Canvas(app, bg='blue')
w.pack(expand=1, fill=BOTH)

shape = "s"

def sKey(event):
    global shape
    print("Now drawing squares")
    shape = "s"

def cKey(event):
    global shape
    print("Now drawing circles")
    shape = "c"

app.bind("<KeyPress-s>", sKey)
app.bind("<KeyPress-c>", cKey)

fillColour = None
colour = "yellow"

def fKey(event):
    global fillColour
    print("Now drawing transparent shapes")
    fillColour = None

def FKey(event):
    global fillColour
    print("Now drawing filled shapes")
    fillColour = colour

def changeColour(col):
    global fillColour, colour
    print("Now drawing in", col)
    colour = col
    if fillColour != None:
        fillColour = colour

def rKey(event):
    changeColour("red")

def yKey(event):
    changeColour("yellow")

app.bind("<KeyPress-f>", fKey)
app.bind("<KeyPress-F>", FKey)
app.bind("<KeyPress-r>", rKey)
app.bind("<KeyPress-y>", yKey)

X = 50
Y = 50

def mouseClick(event):
    mx = event.x
    my = event.y
    if shape == "s":
        w.create_rectangle(mx, my, mx + X, my + Y, \
                           width=5, outline=colour, fill=fillColour)
    else:
        w.create_oval(mx, my, mx + X, my + Y, width=5, \
                      outline=colour, fill=fillColour)

w.bind("<Button-1>", mouseClick)

app.mainloop()