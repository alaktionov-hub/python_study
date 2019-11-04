#!/usr/bin/env python3
x = int(input())
# Dlya testa mogno icpolzovat 4icla 15 ili 45

# Modulus
# 85 // 10 = 8
# 85 % 10 = 5

if x % 2 and x % 3 == 0 and x % 10 != 0:
    print("URA !!!")
