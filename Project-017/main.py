from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title="Make a Bet", prompt="Who is gonna win the Race, Enter the color: ")
colors = ["red", "yellow", "blue", "green", "pink", "orange"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for i in range(0, 6) :
    my_turtle1 = Turtle(shape="turtle")
    my_turtle1.color(colors[i])
    my_turtle1.penup()
    my_turtle1.goto(x=-230, y= y_position[i])
    all_turtle.append(my_turtle1)

if user_bet :
    is_race_on = True

while is_race_on :
    for turtle in all_turtle :
        if turtle.xcor() > 230 :
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet :
                print("You Won\n")
            else :
                print("You Lose\n")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()