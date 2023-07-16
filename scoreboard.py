from turtle import Turtle
FONT = ("Courier", 24, "normal")
STARTING_POS = (-280, 265)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(STARTING_POS)
        self.score = 1
    def update(self):
        self.clear()
        self.write(f"Level: {self.score}", font=FONT)
    def game_over(self):
        self.goto(-40, 0)
        self.write("Game Over", font=FONT, align="center")

