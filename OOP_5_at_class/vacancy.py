#!/usr/bin/env python3
import datetime
import random
import sqlite3

# Enter all inputs for vacancy
vacancy_title = input('Enter title of vacancy! ')
salary = int(input('Salary is  '))
vacancy_main_skill = input('Main skill is ')
vacancy_technologies = input('Enter technologies ')
vacancy_recruiter = input('Recruiter is ')

conn = sqlite3.connect("data/all_worker.db")
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM vacancies")
# count number of rows and make id bigger on 1
vacancy_id = cursor.fetchone()[0]+1
# new vacancy created
vacancy_params = (vacancy_id, vacancy_title, salary,
                  vacancy_main_skill, vacancy_technologies, vacancy_recruiter)
cursor.execute(
    "INSERT INTO vacancies VALUES (?,?,?,?,?,?,'null',1)", vacancy_params)
conn.commit()
print(f'Vacancy {vacancy_title} is in db now!')

# select all candidates from db with same main skill as for vacancy
candidates_db = cursor.execute(
    "SELECT * FROM candidates WHERE main_skill = '{vac_skill}'".format(vac_skill=vacancy_main_skill))
# create list of candites to make random choice from one of them
candidates_list = []
for candidate in candidates_db:
    candidates_list.append(candidate)
# print(random.choice(candidates_list))

# select all programmers from db with same main skill as for vacancy
programmers_db = cursor.execute(
    "SELECT * FROM programmers WHERE main_skill = '{prog_skill}'".format(prog_skill=vacancy_main_skill))
programmers_list = []
for programmer in programmers_db:
    programmers_list.append(programmer)
# print(random.choice(programmers_list))

# prepare params for adding to db
cand = random.choice(candidates_list)[2]
prog = random.choice(programmers_list)[2]
now = datetime.date.today()
tommorrow = datetime.date(now.year, now.month, now.day + 1)
cursor.execute("SELECT COUNT(*) FROM Interviews")
# count number of rows and make id bigger on 1
interview_id = cursor.fetchone()[0]+1
interview_params = (interview_id, vacancy_main_skill, prog,
                    vacancy_recruiter, cand, tommorrow)

cursor.execute(
    "INSERT INTO interviews VALUES(?,?,?,?,?,?,null,null)", interview_params)
conn.commit()
print("Interview was added to db!")

conn.close()
