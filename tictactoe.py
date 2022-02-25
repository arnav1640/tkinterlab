from tkinter import *

# This method is called when the button is pressed
app = Tk()
app.geometry("800x800")
current_turn = "O"


class Game:

    def __init__(self):
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.complete_squares = 0
        for i in range(3):
            for j in range(3):
                eye = i
                jay = j
                self.buttons[i][j] = Button(app, height=10, width=20, text="",
                                            command=lambda i=i, j=j: self.onclick(i, j))
                self.buttons[i][j].grid(row=i, column=j)

    def onclick(self, i, j):
        global current_turn
        if current_turn == "X":
            current_turn = "O"
        elif current_turn == "O":
            current_turn = "X"
        tictactoe.buttons[i][j].configure(text=current_turn)
        finished, winner = self.checkforwin()
        if finished == 1:
            label = Label(app, text=f"winner is {winner}", font=("Arial", 45))
            label.grid(row=3, column=3)

    def checkforwin(self):
        isComplete = 0
        winner = "None"
        for i in range(3):
            for j in range(3):
                if self.buttons[i][j]["text"] != "":
                    self.complete_squares += 1
        if self.complete_squares == 9:
            isComplete = 1
            winner = "TIE"

        if isComplete != 1:
            for i in range(3):
                if self.buttons[i][0]["text"] != "" and self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == \
                        self.buttons[i][2]["text"]:
                    winner = self.buttons[i][0]["text"]
                    isComplete = 1
                    print("ROW MATCH")
                    break
        if isComplete != 1:
            for j in range(3):
                if self.buttons[0][j]["text"] != "" and self.buttons[0][j]["text"] == self.buttons[1][j]["text"] == \
                        self.buttons[2][j]["text"]:
                    winner = self.buttons[0][j]["text"]
                    isComplete = 1
                    print("COLUMN MATCH")
                    break
        if isComplete != 1:
            if self.buttons[0][0]["text"] != "" and self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == \
                    self.buttons[2][2]["text"]:
                winner = self.buttons[0][0]["text"]
                isComplete = 1
                print("DIAGONAL MATCH")
            elif self.buttons[0][2]["text"] != "" and self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == \
                    self.buttons[2][0]["text"]:
                winner = self.buttons[0][2]["text"]
                isComplete = 1
                print("DIAGONAL MATCH")

        return isComplete, winner


tictactoe = Game()
app.mainloop()
