from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto(x=0, y=0)
        self.x_move = 3
        self.y_move = -3
        self.move_speed = 2.5

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        print("Bouncing in the y direction")
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def increase_speed(self):
        self.move_speed *= 1.5

    def reset_position(self):
        self.goto(0, 0)
        self.y_move = -2
