"""
Name: John Hendricks
lab4.py

Problem: I am altering provided code for changing and creating graphics.

Authenticity: I certify that this code below is my own modified version of the previously provided code and
              no one else's.

"""
from graphics import *
import math
# Playing with Graphics

def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move square
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move square")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(20, 40), Point(40,20))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the square
    for i in range(num_clicks):
        p = win.getMouse()
        c = shape.getCenter()  # center of Square

        # move amount is distance from center of square to the
        # point where the user clicked
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        cloned = shape.clone()
        cloned.draw(win)
        shape.move(dx,dy)

    instructions.undraw()
    end = Point(width / 2, height - 10)
    ends = Text(end, "Click again to quit")
    ends.draw(win)
    win.getMouse()
    win.close()


# Building a rectangle from it's corners
def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """
    width_ = 500
    height_ = 500
    new_win = GraphWin("Rectangle()", width_, height_)

    # number_clicks = 2
    inst = Point(width_ / 2, height_ - 10)
    instruction = Text(inst, "Click for first corner of Rectangle")
    instruction.draw(new_win)

    p = new_win.getMouse()
    instruction.undraw()
    new_inst = Point(width_ / 2, height_ - 10)
    new_inst_ = Text(new_inst, "Click for opposite corner of rectangle")
    new_inst_.draw(new_win)
    p1 = p.getX()
    p2 = p.getY()

    p_ = new_win.getMouse()
    p3 = p_.getX()
    p4 = p_.getY()

    shape = Rectangle(Point(p1,p2), Point(p3, p4))
    shape.setFill("blue")
    shape.draw(new_win)
    rect_width = p3 - p1
    rect_height = p4 - p1
    perim = rect_height + rect_width
    area = rect_height * rect_width

    new_inst_.undraw()
    new_inst1 = Point(width_ / 2, height_ - 10)
    new_inst1_ = Text(new_inst1, "the perimeter is {} and the area is {}".format(perim,area))
    new_inst1_.draw(new_win)

    new_win.getMouse()
    new_win.close()

    # pass


def circle():
    width_ = 600
    height_ = 600
    win1 = GraphWin("Circle()", width_, height_)

    inst = Point(width_ / 2, height_ - 10)
    instruction = Text(inst, "Click for center of the circle")
    instruction.draw(win1)

    p = win1.getMouse()
    p1 = p.getX()
    p2 = p.getY()
    instruction.undraw()
    inst1 = Point(width_ / 2, height_ - 10)
    instruction1 = Text(inst, "Click for point of circumference of circle")
    instruction1.draw(win1)

    p_ = win1.getMouse()

    p3 = p_.getX()
    p4 = p_.getY()
    radius = math.sqrt(((p3 - p1)**2) + ((p4 - p1)**2))
    circle1 = Circle(p, radius)
    circle1.draw(win1)

    instruction1.undraw()
    inst2 = Point(width_ / 2, height_ - 10)
    instruction2 = Text(inst2, "the radius of the circle is {}".format(radius))
    instruction2.draw(win1)

    win1.getMouse()
    instruction2.undraw()
    inst3 = Point(width_ / 2, height_ - 10)
    instruction3 = Text(inst3, "Click again to quit")
    instruction3.draw(win1)

    win1.getMouse()
    win1.close()

def pi2():
    first_question = eval(input("Enter value of n for number of terms to sum: "))
    pie = 1
    for i in range(first_question):
        pie *= ((4/(2*(i + 1))) * (-1))

    print(pie)

    print(math.pi - pie)

def main():
    #squares()
    #rectangle()
    #circle()
    pi2()


main()
