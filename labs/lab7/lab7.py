"""
Name: John Hendricks
lab7.py

Problem: More string operations and function calling. Read files too

Authenticity: I certify that the code below is entirely my code and no one else's
"""
from math import pi

# string formatting
def cash_conversion():
    user_input = int(input("Enter an integer: "))
    print("${:.2f}".format(user_input))


# make a secret code
def encode():
    user_input = input("Enter your message you want to be encoded: ")
    key_input = int(input("Enter your key: "))
    new_string = ""
    for char in user_input:
        new_string += chr(ord(char) + key_input)
    print(new_string)


# chapter 6 programming exercise 3
def sphere_area(radius):
    area = 4 * pi * radius ** 2
    return area

def sphere_volume(radius):
    volume = (4/3) * pi * radius ** 3
    return volume

# chapter 6 programming exercise 4
def sum_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def sum_n_cubes(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** 3
    return total


# Intro to file I/O
# both the input and the output txt files were the exact same


# Making a secret-er code
def encode_better():
    user_input = input("Enter your message you want to have encoded: ")
    key_message = input("Enter your cipher key message: ")
    first_string = ""
    for char in range(len(user_input)):
        message = ord(user_input[char]) + (ord(key_message[char]) - 97)
        first_string += chr(message)
    print(first_string)


def main():
    cash_conversion()
    encode()
    sphere_area()
    sphere_volume()
    sum_n()
    sum_n_cubes()
    encode_better()
    pass


main()
