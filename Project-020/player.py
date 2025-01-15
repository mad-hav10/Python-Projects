from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle) :
    def __init__(self):
        super().__init__()
        self.create_turtle()
    
    def create_turtle(self) :
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.restart()
        self.left(90)
        self.forward(MOVE_DISTANCE)

    def move_up(self) :
        new_y = self.ycor() + 10
        self.goto(0, new_y)

    def restart(self) :
        self.goto(STARTING_POSITION)

    def at_end(self) :
        if self.ycor() > FINISH_LINE_Y :
            return True
        else :
            return False
        