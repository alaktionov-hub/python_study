#!/usr/bin/env python3
#
#  Wrote as an Indian :) Maybe 1 day i will fix it all to somthing good one . But at least it work for now
#
import random  # Random module help us generate Fizz Buzz random in range
import sys  # We need sis module to be able read from file
filename = sys.argv[1]
file_size = int(sys.argv[2])  # How many line will be in new file
file_with_fuzz_buzz = open(filename, 'w')

what_fizz_number_start = int(input("Tell me please start of Fizz range?: "))
what_fizz_number_end = int(input("Tell me please end of Fizz range?: "))

what_buzz_number_start = int(input("Tell me please start of Buzz range?: "))
what_buzz_number_end = int(input("Tell me please end of Buzz range?: "))

what_third_number_start = int(input("Tell me please start of Fizz range?: "))
what_third_number_end = int(input("Tell me please end of Fizz range?: "))


# file_with_fuzz_buzz.write("Now the file has more content!")


for line in range(1, file_size+1):
    # a = str(option1), str(option2), str(option3)
    # file_with_fuzz_buzz.write(a)
    file_with_fuzz_buzz.write("{var1} {var2} {var3} \n".format(
        var1=random.randint(what_fizz_number_start, what_fizz_number_end), var2=random.randint(what_buzz_number_start, what_buzz_number_end), var3=random.randint(what_third_number_start, what_third_number_end)))
