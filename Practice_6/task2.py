#!/usr/bin/env python3

# Some docs https://www.geeksforgeeks.org/abs-in-python/


def star(number):
    for i in range(number):
        line = abs(number // 2 - i)
        print(line)  # Just debug info for print
        print(f"{' ' * line}{'*' * (number - line * 2)}")
    return


num = int(input("Enter any number! But i will wotj only with odd!: "))
if num % 2 == 1:  # Check if number is odd
    star(num)  # if yes pass to funcrion start
else:
    print("Number isn't odd!")
