"""
Name: John Hendricks
hangman.py

Problem: Create a game of hangman

Authenticity: I certify that the code below is entirely my own and no one else's. I had no idea how to do the rest
"""
from random import randint

def file_to_list(in_file_name):
    infile = open(in_file_name, "r")
    list_ = infile.readlines()
    infile.close()
    return list_


def random_word(list_):
    random = list_[randint(0, len(list_) - 1)]
    return random


def guessed_word(random):
    guess = input("Enter a letter to guess in the secret word: ").lower()
    for i in range(len(random)):
        if random[i] == guess:
            random[i] = guess

        elif random[i] != guess:
            random[i] = "_"
    return random


def main():
    print(file_to_list("wordlist.txt"))
    print(random_word(file_to_list("wordlist.txt")))
    pass


main()
