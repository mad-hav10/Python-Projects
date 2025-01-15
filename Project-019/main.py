from turtle import Screen, Turtle
from bricks import Bricks
from ball import Ball
import  time
from scoreboard import ScoreCard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)


brick_r = Bricks((350, 0))
brick_l = Bricks((-350, 0))
ball = Ball()
scoreboard = ScoreCard()
scoreboard.update_scoreboard()

screen.listen()
screen.onkey(brick_r.brick_up, 'Up')
screen.onkey(brick_r.brick_down, 'Down')
screen.onkey(brick_l.brick_up, 'w')
screen.onkey(brick_l.brick_down, 's')

game_is_on = True
while game_is_on :
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    #If Ball hits the top or bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()

    #If the ball hits the Bricks
    if ball.distance(brick_r) < 50 and ball.xcor() > 320 or ball.distance(brick_l) < 50 and ball.xcor() < -320 :
        ball.bounce_x()

    #If the ball misses the bricks and hit the left or right walls
    if ball.xcor() > 380 :
        ball.reset_position()
        scoreboard.point_l()
        scoreboard.update_scoreboard()

    if ball.xcor() < -380 :
        ball.reset_position()
        scoreboard.point_r()
        scoreboard.update_scoreboard()

screen.exitonclick()