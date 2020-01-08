#!/usr/bin/env python3
# Need for calculate day off
import datetime


class Employee:
    # Parent Class
    def __init__(self, first_name, last_name, email, phone):
        # in **data any additional information can be put
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
# Task 5.2
    @staticmethod
    def working_days():
        # function that returns amount of working days in the month without some hilidays
        now = datetime.date.today()
        start_month = datetime.date(now.year, now.month, 1)
        diff = (now - start_month).days + 1
        weekend = [5, 6]
        holidays = [datetime.date(now.year, 12, 25), datetime.date(now.year, 10, 14),
                    datetime.date(now.year, 8, 24), datetime.date(now.year, 6, 28), datetime.date(now.year, 5, 1)]
        working_days = 0
        for day in range(diff):
            if (start_month + datetime.timedelta(day)).weekday() not in weekend:
                working_days += 1
            if start_month + datetime.timedelta(day) in holidays:
                working_days -= 1
        return working_days
# Task 5.1
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
# Task 5.1

    @property
    def full_name_and_date(self):
        return f"{self.first_name} {self.last_name} {self.working_days()}"

    def work(self):
        return "I come to the office."
# for Validate task . Check if mail what you pass to self contein in file with mails, raise Error then

    def validate(self):
        print(self.get_emails_from_file())
        if self.email in self.get_emails_from_file():
            raise ValueError
        else:
            print("Email was added to file!")
            self.save_email_to_file()
# Save Mail to file mail . Will open file and save there line from self . (what came)

    def save_email_to_file(self):
        with open('data/emails', 'a') as f:
            f.write(self.email)
            f.write('\n')
# Read all mails from file

    def get_emails_from_file(self):
        with open('data/emails', 'a+') as f:
            f.seek(0)
            data = f.read()
        return data.split('\n')
