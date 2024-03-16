from turtle import *
import turtle


turtle.title('Spiral Rainbow')
turtle.setup(650, 650)
turtle.setworldcoordinates(-350, -350, 350, 350)
turtle.bgcolor('black')
turtle.hideturtle()
turtle.speed(0)

turtle.penup()
turtle.goto((20, -70))
turtle.pendown()

gradient = [
    '#ff0000', '#ff3700', '#ff7700', '#ffa600', '#ffd900',
    '#c3ff00', '#95ff00', '#33ff00', '#00ff40', '#00ff73',
    '#00ffae', '#00ffe5', '#00d0ff', '#008cff', '#005eff',
    '#001eff', '#3700ff', '#6a00ff', '#9000ff', '#bb00ff',
    '#ee00ff', '#ff00d4', '#ff00aa', '#ff0077', '#ff0048'
]
loop = len(gradient)
turtle.width(30)

def spiral_rainbow(amount: int, alpha=0):
    if alpha not in (0, 1, 2, 3): raise ValueError(alpha)

    distance = loop + alpha
    bg_color = 'white'
    rigth_angle = 10
    reverse = False

    def default_draw():
        nonlocal distance
        nonlocal rigth_angle
        nonlocal reverse

        distance -= 1
        rigth_angle -= 1

        turtle.width(turtle.pensize() - 1)
        reverse = False
    def reverse_draw():
        nonlocal distance
        nonlocal rigth_angle
        nonlocal reverse

        distance += 1
        rigth_angle += 1

        turtle.width(turtle.pensize() + 1)
        reverse = True

    for _ in range(amount):
        if bg_color == 'white':
            turtle.getscreen().bgcolor(bg_color)
            bg_color = 'black'
        else:
            turtle.getscreen().bgcolor(bg_color)
            bg_color = 'white'

        for current_color in gradient:
            turtle.color(current_color)

            if distance > 1 and not reverse: default_draw()
            else:
                if distance == loop and reverse: default_draw()
                else: reverse_draw()

            turtle.forward(distance)
            turtle.right(rigth_angle)

try:
    spiral_rainbow(30)
    turtle.done()
except ValueError as ve:
    print(f'\n@InvalidValue:\
          \n\tfunction: spiral_rainbow()\
          \n\tvalue: {ve}\
    ')
    turtle.bye()