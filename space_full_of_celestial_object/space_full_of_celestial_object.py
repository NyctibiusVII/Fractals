from math import ceil
from random import random
from random import choice
from turtle import *
import turtle

turtle.title('Sky Full of Stars')
turtle.setup(650, 650)
turtle.setworldcoordinates(-650, -650, 650, 650)
turtle.bgcolor('#0d0a1e')
turtle.hideturtle()
turtle.speed(0)

operation_signals = ['-', '+']
celestial_object_list = ['star', 'planet']
color_list = [
    '#0c2a5e', '#1b3e7d', # > 30.000K
    '#bcc1c2', '#ebfbff', # ~15.000K
    '#31ad76', '#80d1ad', # 9.000K
    '#d7b661', '#ebd56a', # 7.000K
    '#b55510', '#b5672f', # 6.000K
    '#a31c34', '#ba3049', # 4.000K
    '#270840', '#31094f', # 3.000K
]

# --------------------------------------------------

def random_color(): return choice(color_list)
def random_size(max_size_variation: int): return ceil(random() * max_size_variation)
def random_position_xy(max_size_canvas_x: int, max_size_canvas_y: int = None):
    if max_size_canvas_y is None: max_size_canvas_y = max_size_canvas_x

    signal_x = choice(operation_signals)
    signal_y = choice(operation_signals)
    position_x = int(random() * max_size_canvas_x)
    position_y = int(random() * max_size_canvas_y)

    _x = int(f'{signal_x}{position_x}')
    _y = int(f'{signal_y}{position_y}')

    return _x, _y

# --------------------------------------------------

def planet(size: int, color_primary: str, color_secondary: str):
    # Planet
    turtle.begin_fill()
    turtle.color(color_secondary)
    turtle.fillcolor(color_secondary)
    turtle.circle(size)
    turtle.end_fill()

    # Detail on the planet
    turtle.begin_fill()
    turtle.color(color_primary)
    turtle.fillcolor(color_primary)

    radius = size/2

    for _ in range(ceil(radius/(radius/2)*8)):
        turtle.forward(radius/5)
        turtle.left(10)
    for _ in range(ceil(radius/(radius/2)*6)):
        turtle.left(-7)
        turtle.forward(radius/5.5)
    turtle.left(-65)
    for _ in range(ceil(radius/(radius/2)*9.5)):
        turtle.left(-9.5)
        turtle.forward(radius/3)

    turtle.end_fill()

def star(size: int, color: str):
    turtle.begin_fill()
    turtle.fillcolor(color)

    for _ in range(5):
        # Star
        turtle.color(color)
        turtle.left(72)
        turtle.forward(size)
        turtle.left(-72*2)
        turtle.forward(size)

        # Detail Shining Star
        if size < 6:
            turtle.color('#15112e')
            turtle.left(125.87)
            turtle.forward(size*4)
            turtle.backward(size*4)
            turtle.left(-125.87)

    turtle.color(color)
    turtle.end_fill()

def space(number_of_celestial_objects: int, max_variation_in_the_size_of_objects = 10):
    max_size_variation = max_variation_in_the_size_of_objects

    turtle.penup()
    turtle.goto(random_position_xy(650))
    turtle.pendown()

    celestial_object = choice(celestial_object_list)

    match celestial_object:
        case 'planet':
            planet(random_size(max_size_variation), random_color(), random_color())
        case 'star':
            star(random_size(max_size_variation), random_color())

    if number_of_celestial_objects != 0: space(number_of_celestial_objects - 1)

space(500)
turtle.done()