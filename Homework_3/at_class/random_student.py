#!/usr/bin/env python3
import random

# Jus all student .
students = ['Vasya', 'Kolay', 'Petya', 'Ivan', 'Dimka']

# Create Dict empty
stud_dict = {}
for student in students:
    stud_dict[student] = []
    for _ in range(1, 6):  # _ just for do not allocate space on RAM
        stud_dict[student].append(random.randint(1, 5))
print(stud_dict)
# Example
# {'Vasya': [3, 2, 2, 2, 2], 'Kolay': [3, 4, 3, 4, 3], 'Petya': [2, 2, 4, 2, 3], 'Ivan': [5, 4, 1, 2, 5], 'Dimka': [1, 2, 2, 2, 5]}


# Part 2 calculate
# for name in stud_dict:
#    print(sum(stud_dict.get(name))/len(stud_dict.get(name)))
#
# Without text

for name in stud_dict:
    print("Student {name} has aeverge mark {mark}".format(
        name=name, mark=sum(stud_dict.get(name))/len(stud_dict.get(name))))  # Sum can only sum number So will print only name
# Example
# Student Vasya has aeverge mark 2.2
# Student Kolay has aeverge mark 3.4
# Student Petya has aeverge mark 2.6
# Student Ivan has aeverge mark 3.4
# Student Dimka has aeverge mark 2.4

for name in stud_dict:
    print(stud_dict.get(name))

print("All done")
