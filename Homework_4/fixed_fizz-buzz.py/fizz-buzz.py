#!/usr/bin/env python3
# Fixed version before its write via stdout
import random  # Random module help us generate Fizz Buzz random in range
import sys  # We need sis module to be able read from file

filename = sys.argv[1]  # What File we need use. Argument 1
filename2 = sys.argv[2]  # What File we need use. Argument 1

file_with_fuzz_buzz = open(filename, 'w')
where_keep_answer = open(filename2, 'w')

for line in range(1, 20+1):
    # a = str(option1), str(option2), str(option3)
    # file_with_fuzz_buzz.write(a)
    file_with_fuzz_buzz.write("{var1} {var2} {var3} \n".format(
        var1=random.randint(1, 5), var2=random.randint(1, 6), var3=random.randint(1, 20)))

# Now function return line . Need for fix file write


def fizz_buzz(fizz, buzz, third_number):
    i = 1
    line = ""  # Create variables lin
    while i < (third_number+1):
        if i % fizz == 0 and i % buzz == 0:
            line += "FB "  # add to line
        elif i % fizz == 0:
            line += "F "  # add to line
        elif i % buzz == 0:
            line += "B "  # add to line
        else:
            line += str(i) + " "  # add to line
        i += 1
    return line  # Function return line


file_with_fuzz_buzz = open(filename, 'r')

# lets open file (option 'r')
file_with_fuzz_buzz = open(filename, 'r')
for line in file_with_fuzz_buzz:  # read each line from file
    li = line.split()
    # Pass each number to our function and convert it to int
    # fizz_buzz(int(li[0]), int(li[1]), int(li[2]))
    where_keep_answer.write(
        fizz_buzz(int(li[0]), int(li[1]), int(li[2]))+"\n")  # Call function with new lin
file_with_fuzz_buzz.close()  # close files
file_with_fuzz_buzz.close()  # close files
