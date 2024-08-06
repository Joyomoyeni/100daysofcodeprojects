FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color()
        self.goto(-280, 250)
        self.write(f"Level : {self.level}", align="Left", font=FONT)

    def score(self):
        self.clear()
        self.level += 1
        self.write(f"Level : {self.level}", align="Left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="Center", font=FONT)
    pass
