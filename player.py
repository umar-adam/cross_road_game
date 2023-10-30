from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("turtle")
        self.color("lime green")
        self.penup()
        self.setheading(90)
        self.goto(position)

    def next_level(self):
        self.goto(STARTING_POSITION)

    def move_forwards(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def move_backwards(self):
        self.setheading(270)
        self.forward(MOVE_DISTANCE)

    def move_left(self):
        self.setheading(180)
        self.forward(MOVE_DISTANCE)

    def move_right(self):
        self.setheading(0)
        self.forward(MOVE_DISTANCE)
