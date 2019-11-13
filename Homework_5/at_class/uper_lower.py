#!/usr/bin/env python3
upper_sample = str(input("Please give me lower line: "))
lower_sample = str(input("Please give me Upper line: "))

# Function for upper


def upper_fun(line):
    new_line = line.upper()  # Just use upper
    print(new_line)

# Function for lower


def lower_fun(line):
    new_line = line.lower()  # Just use lower
    print(new_line)


# call function what will print result
upper_fun(upper_sample)
lower_fun(lower_sample)
