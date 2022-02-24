from tkinter import *
# This method is called when the button is pressed
app = Tk()
app.geometry("800x800")
class Game:

    

    def __init__(self):
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = Button(app, height=10, width=20, text="", command=lambda: self.onclick(i, j, "x"))

    def onclick(self, first, second, content):
        self.buttons[first][second].configure(text=content)

    def draw(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].grid(row=i,column=j)
        

tictactoe = Game()
tictactoe.draw()
app.mainloop()