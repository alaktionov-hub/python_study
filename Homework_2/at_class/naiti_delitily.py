#!/usr/bin/env python3
x = int(input())

for number in range(1, x+1):
    if x % number == 0:
        print(number)