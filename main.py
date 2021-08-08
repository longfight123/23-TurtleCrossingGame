"""

This script simulates the popular 'turtle crossing' game.

This script requires that 'turtle' be installed within the Python
environment you are running this script in.

"""

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
screen.onkey(fun=player.move_up, key='Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    # Check for collision with a car
    for car in car_manager.car_list:
        if player.distance(car) < 20:
            scoreboard.game_over()
            time.sleep(10)
            game_is_on = False
    # Check for reaching the end of the level, increase scoreboard and increase speed
    if player.ycor() > 275:
        player.reset_position()
        scoreboard.refresh_score()
        car_manager.increase_speed()
