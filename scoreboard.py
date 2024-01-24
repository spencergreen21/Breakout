from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.strikes = 3
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-550, -250)
        self.show_strikes()

    def update_scoreboard(self, color_score):
        self.score += color_score
        self.show_strikes()

    def show_strikes(self):
        self.clear()
        self.goto(-530, -250)
        self.write(f"Score: {self.score}  Strikes: {self.strikes}", align="center", font=("Arial", 12, "normal"))

    def update_strikes(self):
        if self.strikes > 0:
            self.strikes -= 1
        else:
            self.game_over()

        self.show_strikes()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 36, "normal"))
        self.goto(0, -50)
        self.write(f"Your Score: {self.score}", align="center", font=("Arial", 24, "normal"))







