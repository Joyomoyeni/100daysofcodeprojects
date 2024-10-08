from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.finish = FINISH_LINE_Y

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def reset_post(self):
        self.goto(STARTING_POSITION)




    pass
