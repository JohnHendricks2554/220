"""
Name: John Hendricks
lab3.py

Problem: Develop for loops given user input to get the desired output

Certificate of Authenticity: I certify that this work is entirely my own, and no one else's. I looked up the
 Wallis formula itself to understand the logic of it, but did not look up any code.
"""

# Finding the Average
def average():
    start_question = eval(input("How many grades are you entering?: "))
    new = 0
    for i in range(1, start_question + 1):
        hw_question = eval(input("Enter your grade on HW{}: ".format(i)))
        new += hw_question
        grade_average = new / i
    print("The average grade for the assignments is {}".format(grade_average))

average()

# I work hard for the money!
def tip_jar():
    tip_amount = 0
    for i in range(1,6):
        question = (eval(input("Enter your tip amount: ")))
        tip_amount += question
    print("The total amount in the tip jar is", tip_amount)

tip_jar()

# Compute a square root
def newton():
    x_value = eval(input("Enter the value for x: "))
    approximation = eval(input("How many times do you want to improve the approximation?: "))
    approx = x_value / 2
    for i in range(1, approximation + 1):
        approx = ((approx + (x_value/approx)) / 2)

    print("The square root of x is {}".format(approx))

newton()



# Output a sequence
def sequence():
    num_of_terms = eval(input("Enter the number of terms in a series: "))
    number = 1
    for i in range(1, num_of_terms + 1):
        print(number)
        number = number + 2
        print(number)

sequence()

# Computing pi
def pi():
    num_terms = eval(input("Enter the number of terms in the series: "))
    pie = 1
    for i in range(1,num_terms + 1):
        pi = (((2 * i) / (2 * i + 1)) * ((2 * i) / (2 * i - 1)))
        pie *= pi
    print("The resulting approximation of pi is {}".format(pie * 2))

pi()
