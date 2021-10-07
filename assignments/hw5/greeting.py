"""
John Hendricks
greeting.py

Problem: Creating a heart in graphics that gets absolutely destroyed by arrows.
         Displays happy valentines day

Authenticity: I certify that my code below is entirely my own and no one else's
"""
from graphics import GraphWin, Circle, Point, color_rgb, Polygon, Rectangle, Text

def main():
    win = GraphWin("Greetings", 700, 700, autoflush=False)
    win.setBackground(color_rgb(0,0,255))
    win.getMouse()

    circ = Circle(Point(275,250), 100)
    circ.setFill("red")
    circ.setOutline("red")
    circ.draw(win)
    win.getMouse()

    circ1 = Circle(Point(420,250),100)
    circ1.setFill("red")
    circ1.setOutline("red")
    circ1.draw(win)
    win.getMouse()

    poly = Polygon(Point(187, 300), Point(507, 300), Point(347.5, 500))
    poly.setFill("red")
    poly.setOutline("red")
    poly.draw(win)
    win.getMouse()

    new_inst = Point(700 / 2, 700 - 10)
    new_inst_ = Text(new_inst, "Happy Valentine's Day")
    new_inst_.draw(win)

    win.getMouse()

    arrow = Rectangle(Point(50, 250), Point(120, 260))
    poly = Polygon(Point(120, 240), Point(130, 255), Point(120, 270))
    poly.setFill("black")
    poly.draw(win)
    arrow.setFill("black")
    arrow.draw(win)

    win.getMouse()
    poly.undraw()
    arrow.undraw()
    cloned = arrow.clone()
    cloned.move(20,0)
    poly_cloned = poly.clone()
    poly_cloned.move(20,0)
    cloned.draw(win)
    poly_cloned.draw(win)

    num_clicks = 8
    for _ in range(num_clicks):
        win.getMouse()
        poly_cloned.undraw()
        cloned.undraw()
        cloned = cloned.clone()
        cloned.move(20, 0)
        poly_cloned = poly_cloned.clone()
        poly_cloned.move(20, 0)
        cloned.draw(win)
        poly_cloned.draw(win)

    win.getMouse()
    new_inst_.undraw()
    new_inst = Point(700 / 2, 700 - 10)
    new_inst_ = Text(new_inst, "Click anywhere to close.")
    new_inst_.draw(win)


if __name__ == '__main__':
    main()
