"""
John Hendricks
vigenere.py

Problem: Create a function that makes a graphics window where the user can input their message and key.
         This message will then be encoded using the vigenere encryption and the output will be displayed.

Authenticity: I certify that the code below is entirely mine and no one else's. I did look up some information online
              about the vigenere cipher itself, but I did not look up any code
"""
from graphics import *


def main():
    win = GraphWin("Vigenere", 500, 300)
    win.setCoords(0, 0, 10, 10)

    # message to be encoded
    message = Text(Point(2, 8), "Message to Encode")
    message.draw(win)
    user_input = Entry(Point(6,8), 30)
    user_input.draw(win)

    # keyword to be part of encryption
    keyword = Text(Point(2,6), "Enter Keyword")
    keyword.draw(win)
    key_user_input = Entry(Point(6,6), 30)
    key_user_input.draw(win)

    # drawing encode box
    encode_text = Text(Point(5,4), "Encode")
    encode_text.draw(win)
    encode_box = Rectangle(Point(4,3), Point(6,5))
    encode_box.draw(win)

    win.getMouse()
    encode_box.undraw()
    encode_text.undraw()

    result_message = Text(Point(5,4), "Resulting Message")
    result_message.draw(win)

    no_space_message = message.getText().replace(" ", "")
    updated_message = no_space_message.upper()
    updated_keyword = keyword.getText().upper()

    key = list(updated_keyword)
    if len(updated_message) == len(key):
        return (key)
    else:
        for i in range(len(updated_message) - len(key)):
            key.append(key[i % len(key)])

    text = []
    for i in range(len(updated_message)):
        ord_update = (ord(updated_message[i]) + ord(key[i])) % 26
        text.append(chr(ord_update))
        "".join(text)

    encrypted_result = Text(Point(5,3), text)
    encrypted_result.draw(win)

    inst_pt = Point(5,0.5)
    instructions = Text(inst_pt, "Click Anywhere To Close")
    instructions.draw(win)
    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
