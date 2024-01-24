from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-550, -250)
        self.write("0", align="center", font=("Arial", 24, "normal"))

    def update_scoreboard(self, color_score):
        self.clear()
        self.goto(-550, -250)
        self.score += color_score
        self.write(f"{self.score}", align="center", font=("Arial", 24, "normal"))
