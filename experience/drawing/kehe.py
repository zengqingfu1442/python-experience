"""
一阶科赫曲线
"""


import turtle
from turtle import *


def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size/3, n-1)


def main():
    turtle.setup(600, 600)
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()
    turtle.pensize(2)
    level = 1
    koch(400, level)
    turtle.hideturtle()
    done()


if __name__ == '__main__':
    # turtle.fd(100)
    main()