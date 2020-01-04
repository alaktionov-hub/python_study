#!/usr/bin/env python3
from models.programmer import Programmer
from models.recruter import Recruter
from models.candidat import Candidat
from models.vacancy import Vacancy
from models.check_email import check_emails
from models.fix_email import fix_emails


# Allow you call this file from others modules
if __name__ == '__main__':
    print("Task print info for Recruter" + '\n')

    print("Task print info for Recruter" + '\n')

    recruterHR = Recruter("Vasya", "HR@hell.com",
                          "0668746111", 66.6, hired_this_month=10, info_about="I do not love this")
    print(recruterHR.work())
    print(recruterHR.__str__())
    print(recruterHR.check_salary(666))  # Salary at hell
    print('\n' + "test task 8" + '\n')
    print(recruterHR.check_salary2())  # Salary at hell
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

    print('\n'+"TASK WITH CANDIDATE" + '\n')

    candidat_1 = Candidat("Test Name", "test_name@test.com",
                          "[java,C]", "[Lisp]", "junior")
    candidat_2 = Candidat("test2 test2", "test2_test2@test.com",
                          "[Java,k8s]", "[lisp]", "middle")
    candidat_3 = Candidat(
        "test3 test3", "test3_test3@test.com", "[Lisp,JS]", "[java]", "middle")
    candidat_4 = Candidat(
        "test3 test3", "test3_test3@test.com", "[Lisp,JS]", "[java]", "middle")
    print(candidat_1.name + '\n')
    print(candidat_2.email + '\n')
    print(candidat_3.main_skill + '\n')

    print('\n'+"TASK WITH Vacancy" + '\n')
    vacancy_php = Vacancy("JAVA", "JAVA", "supperme")
    vacancy_Cplus = Vacancy("lisp", "lisp", "junior")
    print(vacancy_Cplus.title)
    print(vacancy_php.main_skill)

    print('\n'+"Task with Mails" + '\n')
    # if not check_emails(candidat_1.email, candidat_2.email, candidat_3.email, candidat_4.email):
    #raise ValueError
    if not check_emails(candidat_1.email, candidat_2.email, candidat_3.email):
        raise ValueError
    print('try 1 variant without error')
    print(fix_emails(candidat_1, candidat_2, candidat_3))

    print('\n'+"Task with Mails so lets try once more" + '\n')
    # will rize error
    print(fix_emails(candidat_1, candidat_2, candidat_3, candidat_4))
