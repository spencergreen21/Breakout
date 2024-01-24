from turtle import Screen
from paddle import Paddle
from ball import Ball
from blocks import Blocks
from scoreboard import Scoreboard
from time import time

colors = {
    "red": 7,
    "orange": 5,
    "green": 3,
    "yellow": 1
}
hits_to_increase_speed = [4, 12]
current_hits = 0

cooldown_duration = 0.1  # Set the cooldown duration in seconds
cooldown_end_time = 0

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1200, height=600)
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard()

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

    # Detect ball hit with blocks
    for row in block_rows:
        for block in row:
            if ball.distance(block) < 30:
                if block.hit(ball):
                    ball.bounce_y()
                    scoreboard.update_scoreboard(block.score)
                    current_hits += 1
                    if current_hits in hits_to_increase_speed:
                        print("Increasing ball speed")
                        ball.increase_speed()

    if cooldown_end_time < time():
        pass

    if (
        ball.distance(paddle) < 30
        and -275 < ball.ycor() < -265  # Check if ball is within the height of the paddle
        and abs(ball.xcor() - paddle.xcor()) < 50
        and cooldown_end_time < time()
    ):
        ball.bounce_y()

    if ball.ycor() < -300:
        ball.reset_position()

    if ball.xcor() < -530 or ball.xcor() > 530:
        ball.bounce_x()

    if ball.distance(paddle) < 30 and ball.ycor() > -250:
        ball.bounce_y()
        cooldown_end_time = time() + cooldown_duration

screen.exitonclick()
