from turtle import *
import turtle

turtle.title('Tree Fractal')
turtle.setup(650, 650)
turtle.bgcolor('#0a0f1f')
turtle.hideturtle()
turtle.speed(0)

turtle.penup()
turtle.goto((-10, -200))
turtle.pendown()

gradient = [
    '#61d420', '#58c41a', '#4fb315', '#699c11', '#6d8a0e',
    '#68730a', '#73650a', '#73540a', '#73460a', '#6b410a',
    '#693f09', '#593608', '#472b06', '#472606', '#361d05'
]
loop = len(gradient)
level = 15
angle = 10
turtle.width(level)
turtle.right(-90)

def yaxis(size: int, lvl: int, angle: int):
    if lvl > 0:
        color = 'black'
        if len(gradient) >= lvl:
            color = gradient[lvl - 1]
            turtle.color(color)
        else: turtle.color(color)

        turtle.forward(size)
        turtle.right(angle)
        turtle.width(turtle.pensize() - 1)

        if lvl > 1:
            yaxis(size * 0.8, lvl - 1, angle + 5)
        else: yaxis(size, lvl - 1, angle + 5)

        turtle.left(2 * angle)

        yaxis(size * 0.8, lvl - 1, angle + 5)
        turtle.color(color)
        turtle.right(angle)
        turtle.forward(-size)
        turtle.width(turtle.pensize() + 1)

yaxis(70, level, angle)
turtle.done()