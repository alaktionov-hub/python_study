#!/usr/bin/env python3
# start Function


def find_all_banknotes(y, numnum):
    if y // numnum:
        print(numnum, "*", y // numnum)
        y = y % numnum
    return y


# Modulus
# 85 // 10 = 8
# 85 % 10 = 5
how_much_money = int(input("Tell me how much money do you need ?: "))


# banknotes that we have in UA
amounts = [500, 200, 100, 50, 20, 10, 5, 2, 1]

for amount in amounts:
    how_much_money = find_all_banknotes(how_much_money, amount)
