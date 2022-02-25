from tkinter import *

app = Tk()
app.title("GUI Example 3")
app.geometry('500x300')

def copyTextToLabel():
    t = v.get()
    if len(v.get()) == 0:
        b1['bg'] = 'red'
    else:
        l1['text'] = v.get()
        b1['bg'] = b1BgColor
        b1['text'] = 'Clear Text'
        b1['command'] = clearEntryText

def clearEntryText():
    v.set("")
    b1['text'] = 'Copy Text'
    b1['command'] = copyTextToLabel

b1 = Button(app, text="Copy Text", command=copyTextToLabel)
b1BgColor = b1['bg']

l1 = Label(app, text="Text is displayed here")

v = StringVar()

e1 = Entry(app, textvariable=v)

l1.pack(side='bottom')
b1.pack(side='bottom')
e1.pack(side='bottom')

app.mainloop()
app.mainloop()