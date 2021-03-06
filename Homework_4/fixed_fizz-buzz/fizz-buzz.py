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
for line in file_with_fuzz_buzz:  # read each line from file
    li = line.split()
    where_keep_answer.write(fizz_buzz(int(li[0]), int(li[1]), int(li[2]))+"\n")

file_with_fuzz_buzz.close()
where_keep_answer.close()
