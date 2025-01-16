from turtle import Turtle

ALLIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle) :
    def __init__(self) :
        super().__init__()
        self.score = 0
        with open(r"C:\Users\sodiu\OneDrive\Documents\Coding\Python Projects\Project-018\data.txt") as data :
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()
        self.hideturtle()
        
    def update_scoreboard(self) :
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.highscore}",align=ALLIGNMENT, font=FONT)
        
    def increase_score(self) :
        self.score += 1
        self.update_scoreboard()

    def reset(self) :
        if self.score > self.highscore :
            self.highscore = self.score
            with open(r"C:\Users\sodiu\OneDrive\Documents\Coding\Python Projects\Project-018\data.txt", "w") as data :
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()
