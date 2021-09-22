"""
Name: John Hendricks
traffic.py

Problem: Create a program that asks the user to enter in the number of roads and to find
         average number of cars found on
         each road for each specified range of days--using accumulation and nested loops.

Authenticity: I certify that my code below is entirely my own code and no one else's
"""

def main():
    lst = []
    sum_lst = []
    first_question = eval(input("How many roads were surveyed? "))
    for i in range(1,first_question + 1):
        var = eval(input("How many days was road {} surveyed? ".format(i)))
        for j in range(1,var + 1):
            var1 = eval(input('How many cars traveled on day {}? '.format(j)))
            lst.append(var1)
            sum_lst.append(var1)
        average = sum(lst) / len(lst)
        final_average = sum(sum_lst) / first_question
        lst.clear()
        print("Road average vehicles per day: {}".format(round(average,2)))
    print("Total number of vehicles travelled on all roads: {}".format(sum(sum_lst)))
    print("Average number of vehicles per road: {}".format(round(final_average,2)))


if __name__ == '__main__':
    main()
