from snake import Snake
from turtle import Screen
import time
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

is_game_on = True
while is_game_on :
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)  < 15 :
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -280 :
        is_game_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:] :
        if snake.head.distance(segment) < 10 :
            is_game_on = False
            scoreboard.game_over()

screen.exitonclick()