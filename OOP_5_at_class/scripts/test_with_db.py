#!/usr/bin/env python3
# https://www.sqlitetutorial.net/sqlite-python/create-tables/
import sqlite3

DB_NAME = 'just_test.db'
connectionObject = sqlite3.connect("just_test.db")
# Obtain a cursor object
cursorObject = connectionObject.cursor()

createTableProgrammers = "CREATE TABLE IF NOT EXISTS programmers(id serial, first_name text, last_name text, email text, phone text, hired_at text, Salary_per_day integer, main_skill text, additional_info text)"


createTableRecruiters = "CREATE TABLE IF NOT EXISTS recruiters (id seriabl, first_name text, last_name text, email text, phone text, hired_at text, Salary_per_day integer)"

createTableCandidates = "CREATE TABLE IF NOT EXISTS candidates (id serial, first_name text, last_name text, email text, phone text, main_skill text)"

createTableVacancies = "CREATE TABLE IF NOT EXISTS vacancies (id serial, title text, salary_per_day integer, main_skills text, technoloies text, recruiter text, hired_at text, status_of_vacncy boolean)"

createTableIterviews = "CREATE TABLE IF NOT EXISTS iterviews (id serial, vacancy text, programer text, recruiter text, candidate text, datetime_of_int text, feedback text, result text)"

cursorObject.execute(createTableProgrammers)
cursorObject.execute(createTableRecruiters)
cursorObject.execute(createTableCandidates)
cursorObject.execute(createTableVacancies)
cursorObject.execute(createTableIterviews)
