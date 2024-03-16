from turtle import *
import turtle

turtle.title('Star Fractal')
turtle.setup(650, 650)
turtle.setworldcoordinates(-650, -650, 650, 650)
turtle.bgcolor('black')
turtle.color('orange')
turtle.hideturtle()
turtle.speed(0)

turtle.penup()
turtle.goto((-200, 50))
turtle.pendown()

def star(size: int, alpha=5):
    if size <= 5: return
    else:
        for _ in range(5):
            turtle.forward(size)
            star(size / alpha, alpha)

            turtle.left(216)

star(360, 2)
turtle.done()