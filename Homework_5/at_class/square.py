#!/usr/bin/env python3
number_list = [2, 3, 34, 17, 29, 6, 12, 3, 4, 67, 98, 32, 5, 65, 7, 5, 4]

# just ** any num what came


def my_square(num):
    return num ** 2

# Try find all prime number from given list


def prime_factor(list):
    final_list = []  # create empty list
    for i in list:
        flip_flop = 0
        if i == 1:
            flip_flop = 1
        for j in range(2, i):  # from 2 to each number in i
            if i % j == 0:  # check if we can % on each on range from 2 to number what came
                flip_flop = 1
                break
        if flip_flop == 0:  # if still 0 uppend its ok for us
            final_list.append(i)  # add each to list
    return final_list


# Just print what it have in our variables with list of prime number.
# print(simple(number_list))
print(prime_factor(number_list))

# Now we have variables where we map my_squer function with simple function what take all prime number from list
squard_list = list(map(my_square, prime_factor(number_list)))


print(squard_list)
