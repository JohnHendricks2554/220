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



print(is_in_linear(7, [1,2,5,6,4,5,7]))