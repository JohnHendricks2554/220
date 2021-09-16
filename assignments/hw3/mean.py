"""
Name: John Hendricks
mean.py

Problem: Using user input, calculate the rms average, harmonic mean and geometric mean with
your defined functions

Certification of Authenticity: I certify that all work in mean.py is entirely my own

QUESTIONS TO BE ANSWERED FIRST:
1. What will my program do?
        Problem: Using user input, calculate the rms average, harmonic mean and geometric mean
        with your defined functions
2. What will be the inputs and outputs?
        Inputs: the input will be the integers the user wishes to find the averages of
        Outputs: the rms average, harmonic mean, and geometric mean of the user's numbers
3. What is a step by step list of what the program will do?
        allow the user to input the numbers to be used to find averages
        using this variable, square each value and add them together, then divide by the amount,
        take the square root
        this is the rms average
        take each value in the original variable,
        and have each value be divided from 1
        take the total number of values in the variable,
        and then divide by the sum of the prior step
        take the square root of that and that is the harmonic average
        multiply all the numbers together from the initial variable and take the exponent of it
        the exponent will be the length of the variable divided from 1
        that will be the geometric average
        round all answers to 3 decimal places and print the averages as output
"""
import math

def main():
    question = eval(input("Enter in the total amount of numbers you are averaging: "))

    squared = 0
    denom_ = 0
    prod = 1
    for i in range(1, question + 1):
        num = eval(input("Enter in number {}: ".format(i)))
        squared += num ** 2
        rms_average = round(math.sqrt(squared / question), 3)

        denom_ += 1/num
        harmonic_average = round(question / denom_, 3)

        prod *= num
        geometric_average = round(math.pow(prod, 1 / question), 3)

    print(rms_average)
    print(harmonic_average)
    print(geometric_average)


if __name__ == '__main__':
    main()
