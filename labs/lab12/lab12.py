"""
Name: John Hendricks
lab12.py

Problem: Work on lists and while loops

Authenticity: I certify that the code below is entirely my own and no one else's
"""
from random import randint
from algorithms import read_data
from algorithms import is_in_linear



# built-in list function
def find_and_remove_first(list, value):
    i = 0
    while i < len(list):
        if list[i] != value:
            i += 1
        elif list[i] == value:
            list[i] = "John"
            i = len(list)
    print(list)


# Forcing good input
def good_input():
    question = eval(input("Enter number in range 1-10: "))
    invalid = False
    nums = [1,2,3,4,5,6,7,8,9,10]

    while question is not invalid:
        if question not in nums:
            if question > len(nums):
                print("Your input was too high")
            else:
                print("Your input was too low")
            question = eval(input("Enter number in range 1-10: "))

        elif question in nums:
            return question


# Counting digits in number
def num_digits():
    question = eval(input("Enter a positive integer: "))
    i = 0
    while question > 0:
        while i <= question:
            question = question // 10
            i += 1
        print(i)
        i = 0
        question = eval(input("Enter a positive integer: "))


# High-Low Game
def hi_lo_game():
    rando_num = randint(0,100)
    guesses = 7
    question = eval(input("Enter number 0-100: "))

    i = 1
    while i < guesses:
        if question > rando_num:
            print("Too high")
            i += 1
            question = eval(input("Enter number 0-100: "))
        elif question < rando_num:
            print("Too low")
            i += 1
            question = eval(input("Enter number 0-100: "))
        else:
            print("Correct")
            print("You win in {} guesses".format(i))

        if i == guesses and question != rando_num:
            print("Sorry, you lose. The number was {}".format(rando_num))








def main():
    list = [1,2,3,3,4,5,6]
    find_and_remove_first(list, 3)
    print(read_data("read_data_test_data.txt"))
    print(is_in_linear(7, [1, 2, 5, 6, 4, 5, 7]))
    good_input()
    num_digits()
    hi_lo_game()
    pass


main()
