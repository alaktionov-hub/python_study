#!/usr/bin/env python3

import sys  # We need sis module to be able read from file
import numpy as np  # need for generate file with fizz buzz


filename_in = sys.argv[1]  # What File we need use. Argument 1
filename_out = sys.argv[2]  # What File we need use. Argument 1

file_with_fuzz_buzz = open(filename_in, 'w')
where_keep_answer = open(filename_out, 'w')

np.savetxt(file_with_fuzz_buzz, np.random.randint(
    1, 12, size=(20, 3)), fmt="%s")
file_with_fuzz_buzz.close()  # Always need close file becaus it save data


def fizz_buzz(fizz, buzz, third_number):
    i = 1
    line = ""
    while i < (third_number+1):
        if i % fizz == 0 and i % buzz == 0:
            line += "FB "
        elif i % fizz == 0:
            line += "F "
        elif i % buzz == 0:
            line += "B "
        else:
            line += str(i) + " "
        i += 1
    return line


# lets open file (option 'r')
file_with_fuzz_buzz = open(filename_in, 'r')
# for line in file_with_fuzz_buzz:  # read each line from file
#    li = line.split()
#    where_keep_answer.write(fizz_buzz(int(li[0]), int(li[1]), int(li[2]))+"\n")
# read_file = file_with_fuzz_buzz.read().split()
# what_calculate = [for line in file_with_fuzz_buzz: line.split("")]

# list_test = []
# list_test = [fizz_buzz(int(li[0]), int(li[1]), int(li[2]))
#             for li in file_with_fuzz_buzz]

# file_with_fuzz_buzz.write(set(map(fizz_buzz, [for line in file_with_fuzz_buzz: line.split("")])))
# print(map(fizz_buzz, [for line in file_with_fuzz_buzz: line.split('')]))
# list([for line in file_with_fuzz_buzz line.split('')])

# points = [line.split("") for line in file_with_fuzz_buzz]
# print(points)
# print(set(map(fizz_buzz(int(list[0]), int([1]), int([2])), [
#      line.split() for line in file_with_fuzz_buzz])))


def read_file(file_name):

    for line in file_name:  # read each line from file
        li = line.split()
        # li = list(map(int, li))  # Map all from line
        li = [int(x) for x in line.split()]
    # print(li)
    # return(int(li[0]), int(li[1]), int(li[2]))
    return li


# print(set(map(fizz_buzz, [line.split for line in file_with_fuzz_buzz])))


print(set(map(fizz_buzz([0, 1, 2]), read_file(file_with_fuzz_buzz))))


#    li=line.split()
# list(map(int, li))

# print(map(fizz_buzz, [for line in file_with_fuzz_buzz: line.split('')]))
# li = line.split()

# file_with_fuzz_buzz.close()
# where_keep_answer.close()
