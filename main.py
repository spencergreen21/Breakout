from turtle import Screen, Turtle
from paddle import Paddle
import turtle as tr

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1200, height=600)
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle()

screen.listen()
screen.onkey(key='Left', fun=paddle.move_left)
screen.onkey(key='Right', fun=paddle.move_right)


game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()






