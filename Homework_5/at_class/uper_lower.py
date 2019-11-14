#!/usr/bin/env python3
upper_sample = str(input("Please give me lower line: "))
lower_sample = str(input("Please give me Upper line: "))

lines = str(input("Please give me Upper and Lower list: "))

# Function for upper


def upper_fun(line):
    new_line = line.upper()  # Just use upper
    return new_line

# Function for lower


def lower_fun(line):
    new_line = line.lower()  # Just use lower
    return new_line


# call function what will print result
print(upper_fun(upper_sample))
print(lower_fun(lower_sample))


lines_sp = lines.split()

map_line = list(map(upper_fun, lines_sp))
map_line2 = list(map(lower_fun, lines_sp))


print(map_line)
print(map_line2)
