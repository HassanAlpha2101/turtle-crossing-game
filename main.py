import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.go_forward, "Up")
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.movement()
    if player.ycor()>=280:
        scoreboard.increase_score()
        car_manager.increase_speed()
        player.my_reset()
    for car in car_manager.car_manager_i:
        if car.distance(player)<20:
            scoreboard.game_over()
            player.my_reset()
            game_is_on = False

    screen.update()

screen.exitonclick()
