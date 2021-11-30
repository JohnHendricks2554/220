"""
Name: John Hendricks
lab13.py

Problem: Perform the capstone and do some sorting and searching

Authenticity: I certify that the code below is entirely my own code and no one else's. I did look at some previous
class notes provided by the professor to get an idea of how to start the function and textbook for selection sort
"""
from algorithms import is_in_binary
from algorithms import selection_sort
from algorithms import calc_area
from graphics import *


def trade_alert(filename):
    infile = open(filename, "r")
    list_ = infile.readline()
    list_ = list_.split()

    for i in range(0, len(list_)):
        if int(list_[i]) > 830:
            print("Warning: stock trades exceed 830 at {} seconds".format(i + 1))
        if list_[i] == str(500):
            print("Pay Attention at {} seconds".format(i + 1))

    infile.close()


def main():
    trade_alert("trades.txt")
    print(is_in_binary(7, [1,2,4,5,6,7,8,9]))
    print(selection_sort([4,7,5,1,8,2,3]))
    print(calc_area(Rectangle(Point(7,5), Point(3,2))))

    pass


main()
