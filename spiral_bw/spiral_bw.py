from turtle import *
import turtle

turtle.title('Spiral Black And White')
turtle.setup(650, 650)
turtle.setworldcoordinates(-650, -650, 650, 650)
turtle.bgcolor('#c8bfe7')
turtle.color('black')
turtle.hideturtle()
turtle.speed(0)

def spiral_bw(size: int):
    turtle.width(0.05)

    for steps in range(size):
        for current_color in ('white', 'black'):
            turtle.width(turtle.pensize() + 0.05)
            turtle.color(current_color)
            turtle.forward(steps)
            turtle.right(100)

spiral_bw(360)
turtle.done()