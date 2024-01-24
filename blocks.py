from turtle import Turtle


class Blocks(Turtle):
    def __init__(self, color, score):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=0.5, stretch_len=3)  # Adjusted stretch_len to create shorter blocks
        self.penup()
        self.score = score

    def hit(self):
        self.goto(1000, 1000)
        return self.score


