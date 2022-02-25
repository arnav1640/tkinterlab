from tkinter import *

app = Tk()
app.title("GUI Example 4")

lFrame = Frame(app, bd=5, relief=GROOVE)
rFrame = Frame(app, bd=5, relief=GROOVE)
lFrame.pack(side='left',fill=BOTH, expand=1)
rFrame.pack(side='right',fill=BOTH, expand=1)

b1 = Label(lFrame, text="A", bg='blue', width=12)
b2 = Label(lFrame, text="B", bg='white', width=12)
b3 = Label(rFrame, text="C", bg='white', width=12)
b4 = Label(rFrame, text="D", bg='blue', width=12)

b1.pack(side='top', fill=BOTH, expand=1)
b2.pack(side='bottom', fill=BOTH, expand=1)
b3.pack(side='top', fill=BOTH, expand=1)
b4.pack(side='bottom', fill=BOTH, expand=1)

app.mainloop()