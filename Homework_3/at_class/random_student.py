#!/usr/bin/env python3
import random


students = ['Vasya', 'Kolay', 'Petya', 'Ivan', 'Dimka']

stud_dict = {}
for student in students:
    stud_dict[student] = []
    for j in range(1, 6):
        stud_dict[student].append(random.randint(1, 5))
print(stud_dict)
