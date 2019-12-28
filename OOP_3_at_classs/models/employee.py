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
