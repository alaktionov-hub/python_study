#!/usr/bin/env python3
upper_sample = str(input("Please give me lower line: "))
lower_sample = str(input("Please give me Upper line: "))


def upper_fun(line):
    new_line = line.upper()
    print(new_line)


def lower_fun(line):
    new_line = line.lower()
    print(new_line)


upper_fun(upper_sample)
lower_fun(lower_sample)
