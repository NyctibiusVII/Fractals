from turtle import *
import turtle
import math

turtle.title('Striped Square Spiral')
turtle.setup(650, 650)
turtle.setworldcoordinates(-650, -650, 650, 650)
turtle.bgcolor('black')
turtle.color('#d7b661')
turtle.hideturtle()
turtle.speed(0)

fill_color = 'black'
alpha = 5

def draw_square(x: int, y: int, direction: int, size: int):
    turtle.up()
    turtle.goto(x, y)
    turtle.seth(direction)
    turtle.back(size / 2)
    turtle.left(90)
    turtle.back(size / 2)
    turtle.seth(direction)
    turtle.down()

    global fill_color
    if fill_color == 'black': fill_color = '#daa520'
    else: fill_color = 'black'

    turtle.begin_fill()

    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)

    turtle.fillcolor(fill_color)
    turtle.end_fill()

def square_spiral(x: int, y: int, direction: int, size: int):
    if size < 5: return

    draw_square(x, y, direction, size)
    square_spiral(x, y, direction + alpha, size / (math.sin(math.radians(alpha)) + math.cos(math.radians(alpha))))

square_spiral(-6, 6, 0, 1320)
turtle.done()
    # if size <= alpha: return
    # if index > 1: turtle.color('black')

    # angle_radians = math.atan(alpha / size)
    # angle_degrees = math.degrees(angle_radians)
    # draw_square(size)
    # turtle.forward(alpha)
    # turtle.left(angle_degrees)
    # striped_square_spiral(size-alpha, index+1)