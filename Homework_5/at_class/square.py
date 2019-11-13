#!/usr/bin/env python3
import math
number_list = [2, 3, 34, 17, 29, 6, 12, 3, 4, 67, 98, 32, 5, 65, 7, 5, 4]

# just ** any num what came


def my_square(num):
    return num ** 2

# Try find all prime number from given list


def simple(list_num):
    final_list = []
    for i in list_num:
        j = 1
        li = []
        for j in range(1, i+1):
            if i % j == 0:
                li.append(j)
        if len(li) < 3:
            final_list.append(i)
    return(final_list)


# Just print what it have in our variables with list of prime number.
print(simple(number_list))


# Now we have variables where we map my_squer function with simple function what take all prime number from list
squard_list = list(map(my_square, simple(number_list)))


print(squard_list)
