"""
John Hendricks
button.py

Problem: Create a user-defined class for the characteristics of a button

Authenticity: I certify that the code below is entirely my own and no one else's
"""
from graphics import *
from random import randint


class Button:
    def __init__(self, shape, text):
        self.shape = shape
        self.text = text

    def get_label(self):
        return self.text

    def draw(self, win):
        win = GraphWin("Three Door Game", 500, 500)
        self.win = win
        button = self.shape
        label_ = self.text
        draw = button.draw(self.win)
        draw_ = label_.draw(self.text)
        return draw_ and draw

    def undraw(self):
        undraw_ = self.button.undraw(self.win)
        return undraw_

    def 
