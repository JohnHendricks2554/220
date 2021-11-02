"""
Name: John Hendricks
lab9.py

Problem: Practice with conditionals

Authenticity: I certify that the code below is entirely my code and no one else's
"""
from graphics import *
import math

def addTen(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


def sumList(nums):
    total = 0
    for i in nums:
        total += i
    return total


def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = int(strList[i])


def writeSumofSquares():
    user_input = input("Enter name of file using .txt at end: ")
    infile = open(user_input, "r")
    outfile = open("sum_out.txt", "w")


    for line in infile:
        var = line.split()
        toNumbers(var)
        squareEach(var)
        total = sumList(var)
        outfile.writelines("Sum of squares: " + str(total) + "\n")

    infile.close()
    outfile.close()


def starter():
    weight_q = float(input("Enter the weight of player: "))
    wins_q = int(input("Enter number of wins player has: "))
    if weight_q >= 150 and weight_q <= 160:
        if wins_q >= 5:
            print("This player can start")
        else:
            print("This player cannot start")
    elif weight_q > 199 or wins_q > 20:
        print("This player can start")
    else:
        print("This player cannot start")


def leapYear():
    leap = False
    year = int(input())
    if year % 100 == 0:
        if year % 400 == 0:
            return not leap
        return leap
    if year % 4 == 0:
        return not leap
    else:
        return leap


def circleOverLap():
    win_height = 500
    win_width = 500
    win = GraphWin("Circle", 500, 500)

    msg = "Click the window to get the center of the circle"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)
    point1 = win.getMouse()
    point1x = point1.getX()
    point1y = point1.getY()
    inst.undraw()

    msg1 = "Click the window to get the edge of the circle"
    inst = Text(Point(win_width / 2, win_height - 20), msg1)
    inst.draw(win)
    point2 = win.getMouse()
    point2x = point2.getX()
    point2y = point2.getY()

    radius = math.sqrt(((point2x - point1x) ** 2) + ((point2y - point1y) ** 2))
    circle1 = Circle(point1, radius)
    circle1.draw(win)
    inst.undraw()
    win.getMouse()

    circle2_point = Point(150, 350)
    circle2x = circle2_point.getX()
    circle2y = circle2_point.getY()
    circle2_radius = 45
    circle2 = Circle(circle2_point, circle2_radius)
    circle2.draw(win)

    circles_distance = math.sqrt(((abs(point1x - circle2x)) ** 2) + (abs((point1y - circle2y) ** 2)))
    if circles_distance > (radius + circle2_radius):
        circle_msg = "These circles do not overlap"
        inst = Text(Point(win_width / 2, win_height - 20), circle_msg)
        inst.draw(win)
    else:
        circle_msg = "These circles do overlap"
        inst = Text(Point(win_width / 2, win_height - 20), circle_msg)
        inst.draw(win)

    win.getMouse()
    inst.undraw()
    message = "Click anywhere to exit"
    inst = Text(Point(win_width / 2, win_height - 20), message)
    inst.draw(win)
    win.getMouse()


def main():
    addTen([2,5,7])
    squareEach([2,5,7])
    print(sumList([2,5,7]))
    toNumbers(["2", "5", "7"])
    writeSumofSquares()
    starter()
    leapYear()
    circleOverLap()
    pass


main()
