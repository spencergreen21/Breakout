from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from blocks import Blocks
import turtle as tr

colors = {
    "red": 7,
    "orange": 5,
    "green": 3,
    "yellow": 1
}

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1200, height=600)
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle()
ball = Ball()

block_rows = []
for color, score in list(reversed(colors.items())):
    block_row = []
    for row in range(2):  # 2 rows for each color
        for col in range(14):  # 14 columns for each row
            block = Blocks(color, score)
            starting_x = -screen.window_width() / 2 + col * 80 + 50  # Adjusted starting x-coordinate with offset
            block.goto(starting_x + 10, 250 - row * 30 - list(colors.values()).index(score) * 60)
            block_row.append(block)
    block_rows.append(block_row)


screen.listen()
screen.onkeypress(key='Left', fun=paddle.move_left)
screen.onkeypress(key='Right', fun=paddle.move_right)


game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    if ball.ycor() < -300:
        ball.reset_position()

screen.exitonclick()






