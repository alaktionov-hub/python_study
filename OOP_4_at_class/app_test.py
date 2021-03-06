#!/usr/bin/env python3
import datetime
import traceback
import sys

# My modules
from models.all_people import Programmer
from models.all_people import Recruiter
from models.all_people import Candidate
from models.vacancy import Vacancy

# Clean our tmp file before we write there somthing
files_with_emails = open('emails', 'w+')
files_with_emails.truncate(0)
#
if __name__ == '__main__':
    recurter_r1 = Recruiter(
        "R1", "R1", "R1R1@gmail.com", "11-11-11", "12-2-12", 200)
    print(recurter_r1.first_name)
    recurter_r1.save_email_to_file()

    programmer_p0 = Programmer("Programmer0", "Programovic0", "p0p0@gmail.com", "01-01-11-1",
                               "03-12-11", 70, "lisp", tech_stack="[lisp,js,C++]", closed_this_month=1)
    programmer_p1 = Programmer("Programmer1", "Programmer1", "p1p1@gmail.com", "01-11-11-2",
                               "04-03-19", 71, "Java", tech_stack="[lisp,bash,SQL]", closed_this_month=2)
    programmer_p2 = Programmer("Programmer2", "Programmer2", "p2p2@gmail.com", "11-03-05-4",
                               "06-06-18", 72, "Js", tech_stack="[C#,Java,lisp,pascal]", closed_this_month=3)
# If you want test error with validate same email . Please uncomment next 4 line
    # programmer_p4 = Programmer("Programmer4", "Programmer4", "p4p4@gmail.com", "01-11-11-2",
    #                           "04-03-19", 71, "Java", tech_stack="[lisp,bash,SQL]", closed_this_month=2)
    # programmer_p5 = Programmer("Programmer5", "Programmer5", "p4p4@gmail.com", "11-03-05-4",
    #                           "06-06-18", 72, "Js", tech_stack="[C#,Java,lisp,pascal]", closed_this_month=3)
    # programmer_p4.validate()
    # programmer_p5.validate()
    #
    print(programmer_p0.hired_at)
    print(programmer_p2.salary_per_day)
    # Validate  programmer
    programmer_p0.validate()
    programmer_p1.validate()
    programmer_p2.validate()
