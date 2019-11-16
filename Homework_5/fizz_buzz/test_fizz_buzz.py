#!/usr/bin/env python3

#
#  NOT HOMEWORK
#  Just try to play with some examples from friend
#

fizz = int(input("Please input fizz value: "))
buzz = int(input("Please input buzz value: "))
third_number = int(input("Please input third_number value: "))


print("\n".join(["F"*(i % fizz == 0)+"B"*(i % buzz == 0) or str(i)
                 for i in range(1, third_number+1)]))
