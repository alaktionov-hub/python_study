#!/usr/bin/env python3
# Task 2 Try read from file and do fozz-buzz to each line
import sys  # We need sis module to be able read from file
filename = sys.argv[1]
file_with_fuzz_buzz = open(filename, 'r')
#
# My old Fizz buzz Function


def fizz_buzz(fizz, buzz, third_number):

    # Please Note we will use print with extra options allow all be onb same line how it was on example
    # Python 3 provides the simplest solution, all you have to do is to provide one extra argument to the print function.
    # You can use the optional named argument end to explicitly mention the string that should be appended at the end of the line.
    # Whatever you provide as the end argument is going to be the terminating string.
    # So if you provide an empty string, then no newline characters, and no spaces will be appended to your input.
    i = 1
# While i less then our third_number + 1 we work in
    while i < (third_number+1):
        if i % fizz == 0 and i % buzz == 0:  # If i multiple to fizz and buzz at same time print FB
            print("FB", end='',)
        elif i % fizz == 0:  # If i multiple to fizz only print F
            print("F", end='',)
        elif i % buzz == 0:  # If i multiple to buzz only print B
            print("B", end='',)
        else:   # If i do not multiple to any checks before that print this value
            print(i, end='',)
        i += 1  # i + 1 starting from 1 . And wait bevore i will be < that third_number what we input from keyb


#
# lets open file (option 'r')
file_with_fuzz_buzz = open(filename, 'r')
for line in file_with_fuzz_buzz:  # read each line from file
    li = line.split()
    # print(li)
    li = list(map(int, li))  # Map all from line
    # Pass each number to our function and convert it to int
    fizz_buzz(int(li[0]), int(li[1]), int(li[2]))
    print()  # need new line  because function print in one line

file_with_fuzz_buzz.close()  # and allways better close file
