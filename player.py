from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
HEADING = 90

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(HEADING)
        self.shape("turtle")


    def go_home(self):
        self.goto(STARTING_POSITION)


    def moveup(self):
        self.forward(MOVE_DISTANCE)
