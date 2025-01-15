from turtle import Turtle, Screen
import turtle
import random

color_list = [(58, 106, 148), (225, 200, 109), (134, 84, 58), (223, 139, 64), (196, 145, 171), (224, 234, 230), (234, 226, 203), (142, 179, 204), (139, 81, 105), (210, 91, 68), (188, 79, 118), (236, 224, 232), (66, 106, 90), (135, 182, 137), (132, 134, 74), (64, 156, 90), (48, 156, 193), (183, 192, 201), (7, 49, 90), (215, 176, 190), (20, 67, 119), (174, 203, 181), (142, 29, 41), (225, 175, 168), (113, 124, 149), (65, 52, 38), (155, 206, 217), (149, 28, 21), (39, 58, 52)]
turtle.colormode(255)

my_turtle = Turtle()
my_turtle.penup()
my_turtle.setheading(225)
my_turtle.forward(300)
my_turtle.setheading(0)

def nextRow() :
    my_turtle.left(90)
    my_turtle.forward(50)
    my_turtle.left(90)
    my_turtle.forward(500)
    my_turtle.right(180)

def movement() :
    for _ in range(10) :
        my_turtle.pendown()
        my_turtle.dot(20, random.choice(color_list))
        my_turtle.penup()
        my_turtle.forward(50)

for _ in range(10) :
    movement()
    nextRow()
        
screen = Screen()
screen.exitonclick()