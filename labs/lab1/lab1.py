"""
Name: John Hendricks
lab1.py

Problem: This function calculates the area of a rectangle
"""

def calc_area():
    length = 20
    width = 5
    area = length * width
    print("Area =", area)

calc_area()

def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)

calc_rec_area()


def calc_volume():
    length = eval(input("Enter the length:"))
    width = eval(input("Enter the width:"))
    height = eval(input("Enter the height:"))
    volume = length * width * height
    print("Volume = ", volume)

calc_volume()


def shooting_percentage():
    total_shots = eval(input("total shots:"))
    made_shots = eval(input("shots made:"))
    percentage = str((made_shots / total_shots ) * 100) + "%"
    print("Shooting Percentage:",percentage)

shooting_percentage()

def coffee():
    #coffee costs $10.50 per pound
    #shipping costs 0.86 per pound
    #fixed cost of $1.50 per pound
    pounds_of_coffee = eval(input("Total pounds of coffee:"))
    coffees = 10.50
    shipping = 0.86
    cost = 1.50
    answer = (coffees * pounds_of_coffee) + (shipping * pounds_of_coffee) + (cost * pounds_of_coffee)
    print("Total cost of coffee:", answer)

coffee()


def kilometers_to_miles():
    #1 mile = 1.61 kiloms
    kilos = eval(input("Number of kilometers traveled:"))
    miles = kilos / 1.61
    print("Total number of miles traveled:", miles)

kilometers_to_miles()