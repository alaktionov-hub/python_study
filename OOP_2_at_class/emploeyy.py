#!/usr/bin/env python3

# TASK 1
# Create class with emmloyee . And save there all data about worker . Name , mail , phone , and salary for 1 day .
# NOT GOOD DAY ! NOT GOOD DAY ! NOT GOOD DAY ! NOT GOOD DAY
#


class Employee:
    def __init__(self, name, email, phone, day_salary):
        self.name = name
        self.email = email
        self.phone = phone
        self.day_salary = day_salary

    def work(self):
        return("So I am here .")
# ADD Class what will calculate salary for some days Calculate how mutch person get

    def check_salary(self, days):
        return self.day_salary*days

# Create class what inhavied from Employee

# Task


class Recruter(Employee):
    def work(self):
        return super().work().replace(".", "and I can find some people who will work for us")

    def __str__(self):
        return "Hello, my name is " + self.name + " " + "And my mail " + self.email + "And you can call me " + self.phone + " and I work here on postition Recruter"

        # Task


class Programmer(Employee):
    def work(self):
        return super().work().replace(".", "and I can CODE")

    def __str__(self):
        return "Hello, my name is " + self.name + " " + "And my mail " + self.email + "And you can call me " + self.phone + " and I work here on position Programmer"


print("Task print info for Recruter" + '\n')

recruterHR = Recruter("Vasya", "HR@hell.com", "0668746111", 66.6)
print(recruterHR.work())
print(recruterHR.__str__())
print(recruterHR.check_salary(666))  # Salary at hell

print('\n' + "Task print info for Programmer" + '\n')

programmer_Ivan = Programmer(
    "Ivan", "to_ivan@ne_tuda.com", "+41212234243", 133)
print(programmer_Ivan.work())
print(programmer_Ivan.__str__())
print(programmer_Ivan.check_salary(6))
