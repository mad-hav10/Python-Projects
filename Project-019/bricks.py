from turtle import Turtle

class Bricks(Turtle) :
    def __init__(self, POSITION):
        super().__init__()
        self.create_brick(POSITION)

    def create_brick(self, POSITION) :
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.right(90)
        self.goto(POSITION)

    def brick_up(self) :
        new_y = self.ycor() + 20
        self.sety(new_y)

    def brick_down(self) :
        new_y = self.ycor() - 20
        self.sety(new_y)
