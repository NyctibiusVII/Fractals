from random import random
from turtle import *
import turtle

turtle.title('Random Draw')
turtle.setup(650, 650)
turtle.setworldcoordinates(-650, -650, 650, 650)
turtle.bgcolor('orange')
turtle.color('black')
turtle.hideturtle()
turtle.speed(0)

def random_draw(size: int):
    for _ in range(size):
        steps = int(random() * 100)
        angle = int(random() * 360)
        width = int(random() * 10)

        turtle.width(width)
        turtle.right(angle)
        turtle.forward(steps)

random_draw(1000)
turtle.done()