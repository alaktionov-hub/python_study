#!/usr/bin/env python3
from models.all_people import Programmer
from models.all_people import Recruiter
from models.all_people import Candidate
from models.vacancy import Vacancy

if __name__ == '__main__':
    recurter_vasya = Recruiter(
        "Vasya", "Vasov", "vasiliy@gmail.com", "23-23-234", "12-12-12", 200)
    print(recurter_vasya.first_name)
    recurter_vasya.save_email_to_file()

    programmer_p0 = Programmer("Programmer0", "Programovic0", "p0p0@gmail.com", "01-01-11-1",
                               "03-12-11", 70, "lisp", tech_stack="[lisp,js,C++]", closed_this_month=1)
    programmer_p1 = Programmer("Programmer1", "Programmer1", "p1p1@gmail.com", "01-11-11-2",
                               "04-03-19", 71, "Java", tech_stack="[lisp,bash,SQL]", closed_this_month=2)
    programmer_p2 = Programmer("Programmer2", "Programmer2", "p2p2@gmail.com", "11-03-05-4",
                               "06-06-18", 72, "Js", tech_stack="[C#,Java,lisp,pascal]", closed_this_month=3)
    print(programmer_p0.hired_at)
    print(programmer_p2.salary_per_day)
    programmer_p0.validate()
    programmer_p1.validate()
    programmer_p2.validate()
