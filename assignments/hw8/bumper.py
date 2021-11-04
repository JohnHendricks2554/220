"""
John Hendricks
bumper.py

Problem: Create a graphics window, practice decision statements

Authenticity: I certify that the code below is entirely my own code and no one else's
"""
from random import randint
from graphics import *


def get_random_color():
    return color_rgb(randint(0, 255), randint(0, 255), randint(0, 255))


def get_random(move_amount):
    return move_amount


def main():
    width = 500
    height = 500
    win = GraphWin("Bumper", width, height)
    win.setBackground("light blue")

    circle1 = Circle(Point(randint(0, 350), randint(0, 350)), randint(0, 100))
    circle1.setFill(get_random_color())
    circle1.draw(win)

    circle2 = Circle(Point(randint(0, 350), randint(0, 350)), randint(0, 100))
    circle2.setFill(get_random_color())
    circle2.draw(win)

    win.getMouse()
    for _ in range(5):
        win.getMouse()
        circle1.move(get_random(randint(-50,50)), get_random(randint(-50,50)))
        circle2.move(get_random(randint(-50,50)), get_random(randint(-50,50)))

    win.getMouse()


if __name__ == '__main__':
    main()
