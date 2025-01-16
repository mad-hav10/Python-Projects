from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake() :
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self) :
        for pos in STARTING_POSITION :
            self.add_segment(pos)
    
    def move(self) :
        for seg_num in range(len(self.segments) - 1, 0, -1) :
            x_cor = self.segments[seg_num - 1].xcor()
            y_cor = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x_cor, y_cor)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self, pos) :
        new_segments = Turtle("square")
        new_segments.color("white")
        new_segments.penup()
        new_segments.goto(pos)
        self.segments.append(new_segments)

    def reset(self) :
        for seg in self.segments :
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
         
    def extend(self) :
        self.add_segment(self.segments[-1].position())

    def up(self) :
        if self.head.heading() != DOWN :
            self.head.setheading(UP)
        
    def down(self) :
        if self.head.heading() != UP :
            self.head.setheading(DOWN)

    def right(self) :
        if self.head.heading() != LEFT :
            self.head.setheading(RIGHT)

    def left(self) :
        if self.head.heading() != RIGHT :
            self.head.setheading(LEFT)
