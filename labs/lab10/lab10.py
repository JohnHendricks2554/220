"""
Name: John Hendricks
Tic_Tac_Toe.py

Problem: Create the game of Tic-Tac-Toe

Authenticity: I certify that the code below is entirely my own and no one else's

I did not understand how to do the rest. I did not want to keep asking too many questions.
"""


def create_board():
    list_ = [1,2,3,4,5,6,7,8,9]
    return list_


def draw_board(board):
    counter = 0
    for i in range(3):
        print(str(board[counter]) + " | " + str(board[counter + 1]) + " | " + str(board[counter + 2]))
        counter += 3
        if counter == 9:
            print("")
        else:
            print("----------")


def mark_space(board, position, character):








def main():
    print("Select the position and character (X or O) to play the game of tic-tac-toe.")
    print("Ex: 1X would be the upper left corner of the board played as X")
    print("Get three in a row and win the game!\n")
    create_board()
    draw_board(create_board())
    pass


main()
