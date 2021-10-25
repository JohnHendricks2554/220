"""
John Hendricks
weighted_average.py

Problem: Computing the weighted averages of student scores from a file and moving it to another file

Authenticity: I certify that the code below is entirely my code and no one else's

I got the right output for the grades.txt file but I failed the rest of the tests
"""


def weighted_average(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w")

    # read in lines
    lucky = infile.readline()
    brianna = infile.readline()

    # formatting of lucky's line
    split_string = (lucky.partition(":"))
    luck_name = split_string[0]
    luck_score = split_string[2]
    luck_list_score = luck_score.split()
    int_l_score = [int(i) for i in luck_list_score]

    # formatting of brianna's line
    split_string_ = (brianna.partition(":"))
    brianna_name = split_string_[0]
    brianna_score = split_string_[2]
    brianna_list_score = brianna_score.split()
    int_b_score = [int(i) for i in brianna_list_score]

    total = 0
    weight_total = 0
    for i in range(0, len(int_l_score), 2):
        total += int_l_score[i] * int_l_score[i + 1]
        weight_total += int_l_score[i]
    if weight_total == 100:
        luck_string = (str(luck_name) + ": " + str(total / 100))
    elif weight_total < 100 or weight_total > 100:
        print(str(luck_name) + ": " + "Error: The Weights are less than 100")
    outfile.write(luck_string + "\n")

    bri_total = 0
    bri_weight_total = 0
    for i in range(0, len(int_b_score), 2):
        bri_total += int_b_score[i] * int_b_score[i + 1]
        bri_weight_total += int_b_score[i]
    if bri_weight_total == 100:
        bri_string = (str(brianna_name) + ": " + str(bri_total / 100))
    elif bri_weight_total < 100 or bri_weight_total > 100:
        print(str(brianna_name) + ": " + "Error: The Weights are less than 100")
    outfile.write(bri_string + "\n")

    class_avg = ((total / 100) +(bri_total / 100) / 2)
    txt_class_avg = "Class average: " + str(class_avg)
    outfile.write(txt_class_avg)

    file1 = open(out_file_name, "r")
    print(file1.read())


weighted_average("grades.txt", "avg.txt")
