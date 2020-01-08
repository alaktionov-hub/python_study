#!/usr/bin/env python3
import datetime
import traceback
from pathlib import Path
import sys

# My modules
from models.all_people import Programmer
from models.all_people import Recruiter
from models.all_people import Candidate
from models.vacancy import Vacancy
from models.sqlite_connector import Sqlite_connector

# CREATE FOLDERS
Path("logs/").mkdir(parents=True, exist_ok=True)
Path("data/").mkdir(parents=True, exist_ok=True)
# Scripts
SCRIPT_FOR_DB_CREATE = 'scripts/create_prod_db.py'
LOG_FILE = 'logs/logs.txt'


# Clean our tmp file before we write there somthing
files_with_emails = open('data/emails', 'w+')
files_with_emails.truncate(0)
#
try:
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
        print(programmer_p0.hired_at)
        print(programmer_p2.salary_per_day)
        # Validate  programmer
        programmer_p0.validate()
        programmer_p1.validate()
        programmer_p2.validate()

        #
        exec(open(SCRIPT_FOR_DB_CREATE).read())
        # Write to DB test
        db_name = 'data/all_worker.db'  # So save all here
        save_table_for_programmer = Sqlite_connector(
            "programmers")  # Save for programmer table
        save_table_for_programmer.add_to_db(programmer_p0, db_name)
        save_table_for_programmer.add_to_db(programmer_p1, db_name)
        save_table_for_programmer.add_to_db(programmer_p2, db_name)

        print("Task 5")
        # TASK ON CLASS 5
        print('\n'+"TASK 5.1 Show property class what return name and second name" + '\n')
        print(programmer_p0.full_name)
        print('\n'+"TASK 5.2 Statick for devs" + '\n')
        print(programmer_p0.working_days())
        print('\n'+"TASK 5.2 Statick for devs Attemp 2" + '\n')
        print(programmer_p0.full_name_and_date)

except ValueError as error:
    with open(LOG_FILE, 'a+') as log_file:
        message = '{}   {}:\n {} \n\n'.format(
            datetime.datetime.now(),
            error.__class__.__name__,
            traceback.format_exc()
        )
        log_file.write(message)
except TypeError as error:
    with open(LOG_FILE, 'a+') as log_file:
        message = '{}   {}:\n {} \n\n'.format(
            datetime.datetime.now(),
            error.__class__.__name__,
            traceback.format_exc()
        )
        log_file.write(message)
else:
    with open(LOG_FILE, 'a+') as log_file:
        message = '{}:\n Unknown error'.format(
            datetime.datetime.now()
        )
        log_file.write(message)
finally:
    print('Exception was handled. Check log for additional info!')
