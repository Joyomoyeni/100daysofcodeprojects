COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.move_dist = STARTING_MOVE_DISTANCE
        self.increment = MOVE_INCREMENT

    def new_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2)
            color = random.choice(COLORS)
            new_car.color(color)
            new_car.penup()
            new_y = random.randint(-250, 250)
            new_car.goto(300, new_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.move_dist)

    def check(self, player):
        for car in self.all_cars:
            if car.distance(player) < 25:
                return True
