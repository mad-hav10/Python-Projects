import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
screen.listen()
screen.onkey(turtle.move_up, "Up")
car = CarManager()
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()

    for cars in car.all_cars :
        if cars.distance(turtle) < 20 :
            game_is_on = False
            scoreboard.game_over()

    if turtle.at_end() :
        turtle.restart()
        car.speed_increase()
        scoreboard.level_inc()

screen.exitonclick()