#!/usr/bin/env python3
import random
import sys  # We need sis module to be able read from file
filename = sys.argv[1]
file_with_fuzz_buzz = open(filename, 'w')


# file_with_fuzz_buzz.write("Now the file has more content!")


x = 20
for line in range(1, x+1):
    #a = str(option1), str(option2), str(option3)
    # file_with_fuzz_buzz.write(a)
    file_with_fuzz_buzz.write("{var1} {var2} {var3} \n".format(
        var1=random.randint(1, 99), var2=random.randint(1, 99), var3=random.randint(1, 99)))
