import math
"""
Name: John Hendricks
arithmetic.py

Problem: Perform various programs that do arithmetic, such as sum of threes, area of a triangle, multiplication table
sum of squares, manually finding the number

"""


# Sum of Threes:
def sum_of_threes():
    upper_bound = eval(input("Please provide an upper bound number: "))
    number_range = range(0,upper_bound + 1,3)
    print(sum(number_range))

# I did not want to do a for loop, haha

sum_of_threes()

# Multiplication table
def multiplication_table():
    print(1," ",2," ",3," ",4," ",5," ",6," ",7," ",8," ",9," ",10)
    for row in range(1,11):
        for col in range(1,11):
            print(row * col, end="\t")
        print()
    print("\n")

multiplication_table()


# Computing the area of a triangle
def triangle_area():
    a_side = eval(input("Enter the length of side a: "))
    b_side = eval(input("Enter the length of side b: "))
    c_side = eval(input("Enter the length of side c: "))

    s_ = (a_side + b_side + c_side) / 2
    Area = math.sqrt(s_*((s_ - a_side)*(s_ - b_side)*(s_ - c_side)))

    print(Area)

triangle_area()


# Sum of Squares
def sumSquares():
    start = eval(input("Enter the starting number: "))
    end = eval(input("Enter the ending number: "))
    sum = 0
    for i in range(start,end + 1):
        sum = sum + i**2
    print(sum)

sumSquares()

# Manually Finding the power
def power():
    base = eval(input("Enter the base value: "))
    exponent = eval(input("Enter the exponent value: "))
    power = 1
    for i in range(exponent):
        power = power * base

    print("{} ^ {} = {}".format(base,exponent,power))

power()