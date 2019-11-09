#!/usr/bin/env python3
f = int(input("give me f: "))
b = int(input("give me b: "))
n = int(input("give me n: "))


for i in range(1, n+1):
    if i % b == 0 and i % f == 0:
        print("fb", end=" ")
    elif i % f == 0:
        print("f", end=" ")

    elif i % b == 0:
        print("b", end=" ")
    else:
        print(i, end=" ")
        i+1
