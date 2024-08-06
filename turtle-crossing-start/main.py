import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(key="Up", fun=player.move_forward)

game_is_on = True
n = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.new_car()
    car_manager.move_cars()

    if car_manager.check(player):
        scoreboard.game_over()
        game_is_on = False

    if player.ycor() == player.finish:
        scoreboard.score()
        player.reset_post()
        car_manager.move_dist += car_manager.increment

screen.exitonclick()
