from graphics import *

def read_data(filename):
    infile = open(filename, "r")
    line = infile.read()
    line = line.split()

    i = 0
    while i < len(line):
        line[i] = eval(line[i])
        i += 1

    infile.close()
    return line

# linear search
def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        if values[i] != search_val:
            i += 1
            if i >= len(values):
                return False
        else:
            return True

# binary searches
def is_in_binary(search_val, values):
    high = len(values) - 1
    low = 0

    while low <= high:
        middle = (low + high) // 2
        middle_num = values[middle]
        if search_val == middle_num:
            return middle
        if search_val < middle_num:
            high = middle - 1
        if search_val > middle_num:
            low = middle + 1

    return False

# sorting
def selection_sort(values):
    start = 0
    n = len(values)
    while start != len(values):
        for i in range(n - 1):
            mp = i
            for j in range(i + 1, n):
                if values[j] < values[mp]:
                    mp = j
                    start += 1
            values[i], values[mp] = values[mp], values[i]
    print(values)






# area of rectangle
def calc_area(rect):
    first_point = rect.getP1()
    second_point = rect.getP2()

    p1x = first_point.getX()
    p1y = first_point.getY()

    p2x = second_point.getX()
    p2y = second_point.getY()

    rect_width = abs(p2x - p1x)
    rect_height = abs(p2y - p1y)

    rect_area = rect_height * rect_width
    return rect_area

