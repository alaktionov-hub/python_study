#!/usr/bin/env python3
import datetime


now = datetime.date.today()
start_month = datetime.date(now.year, now.month, 1)
diff = (now - start_month).days + 1
# Calculate work day in month Task 8
weekend = [5, 6]
holidays = [datetime.date(now.year, 12, 25), datetime.date(now.year, 10, 14),
            datetime.date(now.year, 8, 24), datetime.date(now.year, 6, 28), datetime.date(now.year, 5, 1)]

working_days = 0
for day in range(diff):
    if (start_month + datetime.timedelta(day)).weekday() not in weekend and start_month + datetime.timedelta(day) not in holidays:
        working_days += 1
# TASK 1
# Create class with emmloyee . And save there all data about worker . Name , mail , phone , and salary for 1 day .
# NOT GOOD DAY ! NOT GOOD DAY ! NOT GOOD DAY ! NOT GOOD DAY
#


class Employee:
    def __init__(self, name, email, phone, day_salary, **data):  # data = for task 9
        self.name = name
        self.email = email
        self.phone = phone
        self.day_salary = day_salary
        self.data = data

    def work(self):
        return("So I am here .")
# ADD Class what will calculate salary for some days Calculate how mutch person get

    def check_salary(self, days):
        return self.day_salary*days

    def check_salary2(self, days=working_days):
        return self.day_salary*days

# Create class what inhavied from Employee

# Task


class Recruter(Employee):
    def work(self):
        return super().work().replace(".", "and I can find some people who will work for us")

    def __str__(self):
        return "Hello, my name is " + self.name + " " + "And my mail " + self.email + "And you can call me " + self.phone + " and I work here on postition Recruter"

    def __lt__(self, other):
        return self.day_salary < other.day_salary

        # Task


class Programmer(Employee):
    def work(self):
        return super().work().replace(".", "and I can CODE")

    def __str__(self):
        return "Hello, my name is " + self.name + " " + "And my mail " + self.email + "And you can call me " + self.phone + " and I work here on position Programmer"
# Need find way to fix for compare also salary not only tech stack

    def __lt__(self, other):
        return self.day_salary < other.day_salary

    def __gt__(self, other):
        return len(self.data.get("tech_stack")) > len(other.data.get("tech_stack"))

    def __lt__(self, other):
        return len(self.data.get("tech_stack")) < len(other.data.get("tech_stack"))

    def __eq__(self, other):
        return len(self.data.get("tech_stack")) == len(other.data.get("tech_stack"))


print("Task print info for Recruter" + '\n')

recruterHR = Recruter("Vasya", "HR@hell.com",
                      "0668746111", 66.6, hired_this_month=10, info_about="I do not love this")
print(recruterHR.work())
print(recruterHR.__str__())
print(recruterHR.check_salary(666))  # Salary at hell
print('\n' + "test task 8" + '\n')
print(recruterHR.check_salary2())  # Salary at hell
#print('\n' + "test task 9" + '\n')
#recruterHR.hired_this_month = 13
# print(recruterHR.hired_this_month)
#print(recruterHR.hired_this_month + 1)
#print(recruterHR.hired_this_month - 3)
# print('\n' + "test task 9" + '\n')
print('\n' + "test task 9" + '\n')
print(recruterHR.data)
print('\n' + "end task 9" + '\n')

print("Task print info for Recruter2" + '\n')

recruterHR2 = Recruter("Vasya", "HR@hell.com", "0668746111", 666.6)
print(recruterHR2.work())
print(recruterHR2.__str__())
print(recruterHR2.check_salary(666))  # Salary at hell

print('\n' + "Task print info for Programmer" + '\n')

programmer_Ivan = Programmer(
    "Ivan", "to_ivan@ne_tuda.com", "+41212234243", 133, tech_stack=['c++', 'C', 'python'])

programmer_Tolik = Programmer(
    "Tolik", "Tolik@ne_tuda.com", "+41666666", 333, tech_stack=['c++', 'C', 'python', 'bash'])

print(programmer_Ivan.work())
print(programmer_Ivan.__str__())
print(programmer_Ivan.check_salary(6))
print('\n' + "test task 8" + '\n')
print(programmer_Ivan.check_salary2())  # Salary at hell

print('\n' + "test task 10" + '\n')
print(programmer_Ivan.data.get('tech_stack'))
print(programmer_Tolik.data.get('tech_stack'))
print('\n' + "end task 10" + '\n')


# Compare Salary
print('\n' + "Task With Salary Compare" + '\n')
if recruterHR < recruterHR2:
    print("More big")


# Compare Salary
print('\n' + "Task 11 test" + '\n')
if programmer_Ivan < programmer_Tolik:
    print("More big")
