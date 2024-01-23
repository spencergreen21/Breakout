from turtle import Turtle

MOVE_DIST = 70


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(x=0, y=-275)  # Adjust the starting y-coordinate

    def move_left(self):
        x = self.xcor()
        x -= MOVE_DIST
        self.setx(x)

    def move_right(self):
        x = self.xcor()
        x += MOVE_DIST
        self.setx(x)


