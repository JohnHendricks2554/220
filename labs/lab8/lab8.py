"""
Name: John Hendricks
lab8.py

Problem: Writing functions involving files

Authenticity: I certify that the code below is entirely my code and no one else's
"""
from encryption import encode
from encryption import encode_better

def number_words(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w")

    count = 0
    for line in infile:
        for i in line.split():
            count += 1
            outfile.write(str(count) + " " + str(i) + "\n")
    infile.close()
    outfile.close()


def hourly_wages(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w")

    # raise is $1.65 per hour for each employee
    for line in infile:
        var = line.split()
        names = (var[0:2])
        new_wage = float(var[2]) + 1.65
        weekly_wage = new_wage * int(var[3])
        names_ = " ".join(names)
        outfile.writelines(names_ + " " + str(weekly_wage) + "\n")
    infile.close()
    outfile.close()


def calc_check_sum(isbn):
    total = 10
    sum = 0
    for i in isbn:
        func = int(i) * total
        total -= 1
        sum += func
    return sum


def send_message(file, friend):
    infile = open(file, "r")
    outfile = open(friend + ".txt", "w")

    data = infile.read()
    outfile.write(data)
    infile.close()
    outfile.close()


def send_safe_message(file, friend, key):
    infile = open(file, "r")
    outfile = open(friend + ".txt", "w")

    var = infile.read()
    message = encode(var, key)
    outfile.write(message)

    infile.close()
    outfile.close()


def send_uncrackable_message(file, friend, pad):
    infile = open(file, "r")
    outfile = open(friend + "txt", "w")

    data = infile.read()
    message = encode_better(data, pad)
    outfile.write(str(message))

    infile.close()
    outfile.close()


def main():
    number_words("Walrus.txt", "output.txt")
    hourly_wages("hourly_wages.txt", "hourly_output.txt")
    calc_check_sum("0072946520")
    send_message("message.txt", "bob")
    send_safe_message("safest_message.txt", "bob", 3)
    send_uncrackable_message("secret_message.txt", "jacob", "pad.txt")

    pass


main()
