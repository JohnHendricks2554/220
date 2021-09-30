"""
Name: John Hendricks
lab5.py

Problem: Creating graphics and entry objects based on the question itself, and create functions that alter lists and
strings

Authenticity: I certify that this code below is mine and no one else's besides the already provided code that was
included in this lab.
"""

from graphics import *
import math

def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    # Add code here to get the dimensions and draw the target
    circ1 = Circle(Point(250,250), 245)
    circ1.setFill("white")
    circ1.setOutline("black")
    circ1.draw(win)

    circ2 = Circle(Point(250,250), 196)
    circ2.setFill("black")
    circ2.draw(win)

    circ3 = Circle(Point(250,250), 147)
    circ3.setFill("blue")
    circ3.draw(win)

    circ4 = Circle(Point(250,250), 98)
    circ4.setFill("red")
    circ4.draw(win)

    circ5 = Circle(Point(250,250), 49)
    circ5.setFill("yellow")
    circ5.draw(win)

    # Wait for another click to exit
    size = Point(win_width / 2, win_height - 10)
    text = Text(size, "Click again to close the window")
    text.draw(win)
    win.getMouse()
    win.close()


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    # Add code here to accept the mouse clicks, draw the triangle.
    # and display its area in the graphics window.
    point1 = win.getMouse()
    point1.draw(win)

    point2 = win.getMouse()
    point2.draw(win)

    point3 = win.getMouse()
    point3.draw(win)

    triangle = Polygon(point1, point2, point3)
    triangle.draw(win)

    tri_list = triangle.getPoints()
    print(tri_list)

    # for line between point 1 and point 2
    dx1 = point2.getX() - point1.getX()
    dy1 = point2.getY() - point1.getY()

    # for line between point 1 and point 3
    dx2 = point3.getX() - point1.getX()
    dy2 = point3.getY() - point1.getY()

    # for line between point 2 and point 3
    dx3 = point3.getX() - point2.getX()
    dy3 = point3.getY() - point2.getY()

    # length of line 1
    length1 = math.sqrt((dx1 ** 2) + (dy1 ** 2))
    # length of line 2
    length2 = math.sqrt((dx2 ** 2) + (dy2 ** 2))
    # length of line 3
    length3 = math.sqrt((dx3 ** 2) + (dy3 ** 2))

    perimeter = length1 + length2 + length3

    # for area
    s = perimeter / 2
    area = math.sqrt(s * (s - length1) * (s - length2) * (s - length3))

    # input text in window
    size = Point(win_width / 2, win_height - 10)
    text = Text(size, "The perimeter and area of the triangle are {} and {}".format(round(perimeter,2), round(area,2)))
    text.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)
    num_clicks = 5

    for i in range(1, num_clicks + 1):
        # redTexPt is 50 pixels to the left and forty pixels down from center
        red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
        red_text = Text(red_text_pt, "Red: ")
        red_text.setTextColor("red")
        input_red = Entry(Point(200, 240), 5)
        input_red.draw(win)

        # green_text_pt is 30 pixels down from red
        green_text_pt = red_text_pt.clone()
        green_text_pt.move(0, 30)
        green_text = Text(green_text_pt, "Green: ")
        green_text.setTextColor("green")
        input_green = Entry(Point(200, 270), 5)
        input_green.draw(win)

        # blue_text_pt is 60 pixels down from red
        blue_text_pt = red_text_pt.clone()
        blue_text_pt.move(0, 60)
        blue_text = Text(blue_text_pt, "Blue: ")
        blue_text.setTextColor("blue")
        input_blue = Entry(Point(200, 300), 5)
        input_blue.draw(win)

        # display rgb text
        red_text.draw(win)
        green_text.draw(win)
        blue_text.draw(win)

        win.getMouse()

        shape.setFill(color_rgb(int(input_red.getText()), int(input_green.getText()), int(input_blue.getText())))

    # Wait for another click to exit
    win.getMouse()
    win.close()

def process_string():
    initial_string = str(input("Enter your string: "))
    first_char = initial_string[0]
    print("The first character is {}".format(first_char))

    last_char = initial_string[-1]
    print("The last character is {}".format(last_char))

    exclusive_char = initial_string[2:6]
    print("The 2-5 characters in the list are {}".format(exclusive_char))

    concat = first_char + last_char
    print("The first and last character printed together: {}".format(concat))

    repeat_first3 = initial_string[0:2] * 10
    print("The first 3 characters repeated 10 times: {}".format(repeat_first3))

    # for each character being on a new line
    for i in initial_string:
       print(i, end = "\n")

    len_string = len(initial_string)
    print("The length of the string is: {}".format(len_string))


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    # number 1
    x = values[1] + values[3]
    print(x)
    # number 2
    x = values[0] + values[2]
    print(x)
    # number 3
    x = values[1] * 5
    print(x)
    # number 4
    x = values[2:5]
    print(x)
    # number 5
    x = []
    x.append(values[2])
    x.append(values[3])
    x.append(values[0])
    print(x)
    # number 6
    x = []
    x.append(values[2])
    x.append(values[0])
    x.append(float(values[5]))
    print(x)
    # number 7
    x = values[0] + values[2] + float(values[-1])
    print(x)
    # number 8
    x = len(values)
    print(x)

def another_series():
    first_question = eval(input("Enter in the total number of terms to be added: "))
    the_values = list(eval(input("Enter in the numbers you want to add separated by commas: ")))
    print(the_values)

    sum_ = sum(the_values)
    print(sum_)


def main():
    target()
    triangle()
    color_shape()
    process_string()
    process_list()
    another_series()
    pass


main()
