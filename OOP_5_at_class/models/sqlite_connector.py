#!/usr/bin/env python3
# https://www.sqlitetutorial.net/sqlite-python/create-tables/
import sqlite3


class Sqlite_connector:

    # class for work with db
    def __init__(self, table_name):
        # name of the table in the properties of class
        self.table_name = table_name

    def add_to_db(self, obj, db_name):
        # add rows to db
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        try:
            if cursor.execute("SELECT * FROM {table_name}".format(table_name=self.table_name)):
                cursor.execute(
                    "SELECT COUNT(*) FROM {table}".format(table=self.table_name))
                id = cursor.fetchone()[0]+1
                val = ""
                if self.table_name == 'programmers':
                    obj = [(id, obj.first_name, obj.last_name, obj.email, obj.phone, obj.hired_at,
                            obj.salary_per_day, obj.main_skill, str(obj.data))]
                    val = "(?,?,?,?,?,?,?,?,?)"
                elif self.table_name == 'recruiters':
                    obj = [(id, obj.first_name, obj.last_name, obj.email,
                            obj.phone, obj.hired_at, obj.salary_per_day)]
                    val = "(?,?,?,?,?,?,?)"
                elif self.table_name == 'candidates':
                    obj = [(id, obj.first_name, obj.last_name,
                            obj.email, obj.phone, obj.main_skill)]
                    val = "(?,?,?,?,?,?,?)"
                elif self.table_name == 'vacancies':
                    obj = [(id, obj.title, obj.salary_per_day, obj.mail_skills, obj.technologies,
                            obj.recruiter, obj.hired_at, obj.status_of_vacancy)]
                    val = "(?,?,?,?,?,?,?)"
                elif self.table_name == 'iterviews':
                    obj = [(id, obj.vacancy, obj.programmer, obj.recruiter, obj.candidate,
                            obj.datetime_of_int, obj.feedback, obj.result)]

                cursor.executemany("INSERT INTO {table} VALUES {val}".format(
                    table=self.table_name, val=val), obj)
                conn.commit()
        except:
            print("Table with name {table} doesn't exist!".format(
                table=self.table_name))
        finally:
            conn.close()

    def read_from_db(self, db_name):
        # print all rows from the table if it exists
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        try:
            cursor.execute(
                "SELECT * FROM {table_name}".format(table_name=self.table_name))
            print(cursor.fetchall())
        except:
            print("Table with name {table} doesn't exist!".format(
                table=self.table_name))
        finally:
            conn.close()

    def delete_from_db(self, db_name):
        # delete table from db
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        try:
            cursor.execute("DROP TABLE {table_name}".format(
                table_name=self.table_name))
        except:
            print("Table with name {table} doesn't exist!".format(
                table=self.table_name))
        finally:
            conn.close()
