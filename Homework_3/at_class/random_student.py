#!/usr/bin/env python3
import random


students = ['Vasya', 'Kolay', 'Petya', 'Ivan', 'Dimka']

stud_dict = {}
for student in students:
    stud_dict[student] = []
    for j in range(1, 6):
        stud_dict[student].append(random.randint(1, 5))
print(stud_dict)

# Part 2 calculate
# for name in stud_dict:
#    print(sum(stud_dict.get(name))/len(stud_dict.get(name)))
#
# Without text

for name in stud_dict:
    print("Student {name} has aeverge mark {mark}".format(
        name=name, mark=sum(stud_dict.get(name))/len(stud_dict.get(name))))

print("All done")
