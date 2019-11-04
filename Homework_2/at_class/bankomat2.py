#!/usr/bin/env python3
print("Tell me how much money do you need ?")
how_much_money = int(input())

# start Function


def find_all_banknotes(y, numnum):
    if y // numnum:
        print(numnum, "*", y // numnum)
        y %= numnum
# Modulus
# 85 // 10 = 8
# 85 % 10 = 5


# banknotes that we have in UA
amounts = [500, 200, 100, 50, 20, 10, 5, 2, 1]

for amount in amounts:
    find_all_banknotes(how_much_money, amount)
