from turtle import Turtle 

class ScoreCard(Turtle) :
    def __init__(self):
        super().__init__()
        self.create_scorebard()

    def create_scorebard(self) :
        self.hideturtle()
        self.penup()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        
    def update_scoreboard(self) :
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=('Courier', 80, 'normal'))

    def point_l(self) :
        self.l_score += 1

    def point_r(self) :
        self.r_score += 1