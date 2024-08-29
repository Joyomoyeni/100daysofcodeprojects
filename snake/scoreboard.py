from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(file="data.txt", mode="r") as file:
            number = int(file.read())
        self.highscore = number
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open(file="data.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()
