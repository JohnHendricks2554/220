"""
Name: John Hendricks
Lab6.py

Problem: Altering strings using functions

Authenticity: I certify that the code below is entirely my own code and no one else's
"""

# name switching

def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    full_name = input("Enter in first and last name: ")
    list = full_name.split()
    list.reverse()
    reverse = ", ".join(list)
    print(reverse)


# splitting a domain name

def company_name():
    question = input("Enter in the three part website domain name: ")
    new_list = question.split(".")
    print(new_list[1])


# slice and dice

def initials():
    initial_question = eval(input("How many names are being entered?: "))
    for i in range(1, initial_question + 1):
        first = input("Enter the first name of student {}: ".format(i))
        last = input("Enter {}'s last name: ".format(first))
        initials_ = first[0] + last[0]
        print("{}'s initials are {}".format(first, initials_))

# slice and dice 2
# I already know that this is wrong, didn't have time
def names():
    string = ""
    name_question = (input("Enter in people's names, separated by commas: ")).split(",")
    for name in name_question:
        names = name.split()
        first_name = names[0]
        last_name = names[1]
        full_name = first_name[0] + last_name[0]
        initials = full_name + " "
        print("The initials are {}".format(initials))



# every third
# couldn't figure this one out, didn't have time to figure it out.
def thirds():
    list = []
    question = eval(input("How many sentences will be input: "))
    input_question = input("Enter in the {} sentences: ".format(question))
    split_ = input_question.split(".")
    #print(split_)
    #for i in range(0,len(split_),3):


# didn't have time for this either.
#def word_average():


# didn't have time for this either
#def pig_latin():


def main():
    name_reverse()
    company_name()
    initials()
    names()
    thirds()

main()
