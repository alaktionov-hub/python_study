#!/usr/bin/env python3

print("Tell me how much money do you need?")
how_much_money = int(input())

# banknotes that we have in UA
amounts = [500, 200, 100, 50, 20, 10, 5, 2, 1]

for amount in amounts:
    if how_much_money // amount:
        print(amount, "*", how_much_money // amount)
        how_much_money %= amount

# Modulus
# 85 // 10 = 8
# 85 % 10 = 5
