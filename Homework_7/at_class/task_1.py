#!/usr/bin/env python3
import random
all_student = ["Anna", "Inna", "Olga", "Kira", "Mila"]  # all our student


def random_mark():
    # We generate 5 marks
    return [random.randint(1, 5) for element in range(5)]


students_with_mark = {student: random_mark() for student in all_student}

print(students_with_mark)
print("----------------------------------------------------------------------------")
print("And now with Mark")

# for i in students_with_mark:
#    print(i + " "+str(sum(students_with_mark[i])/len(students_with_mark[i])))
st_aver = {st: sum(
    students_with_mark[st])/len(students_with_mark[st]) for st in all_student}

print(st_aver)

sorted_x = sorted(st_aver.items(), key=lambda mr: mr[1])
print(sorted_x)

print("----------------------------------------------------------------------------")
print("----------------------------------------------------------------------------")

print("Looser is " + str(sorted_x[0][0]) +
      " " + "mark is " + str(sorted_x[0][1]))
print("Winner is " + str(sorted_x[-1][0]) +
      " " + "mark is " + str(sorted_x[-1][1]))
