from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.current_level = 1
        self.penup()
        self.goto(-210, 260)

    def level(self):
        self.clear()
        self.write(arg=f"Level: {self.current_level}", align=ALIGNMENT, font=FONT)

    def next_level(self):
        self.current_level += 1
        self.level()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER!", align=ALIGNMENT, font=FONT)
