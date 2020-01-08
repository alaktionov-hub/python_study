import csv

from .employee import Employee


class Programmer(Employee):
    # class Programmer is inherited from Employee
    def __init__(self, first_name, last_name, email, phone, hired_at, salary_per_day, main_skill, **data):
        # Take all params from main class
        super().__init__(first_name, last_name, email, phone)
        self.hired_at = hired_at
        self.salary_per_day = salary_per_day
        self.main_skill = main_skill
        self.data = data

    def work(self):
        # method work is redefined
        return super().work()[:-1] + " and start WORK WORK WORK."

    def __str__(self):
        # method __str__ is redefined
        return "I'm The best programmer ever" + self.first_name + " " + self.last_name + "."

    def __gt__(self, other):
        # with this methods programmers can be compared by their skills . With super methods
        return len(self.data.get("tech_stack")) > len(other.data.get("tech_stack"))
        # with this methods programmers can be compared by their skills . With super methods

    def __lt__(self, other):
        return len(self.data.get("tech_stack")) < len(other.data.get("tech_stack"))
        # with this methods programmers can be compared by their skills . With super methods

    def __eq__(self, other):
        return len(self.data.get("tech_stack")) == len(other.data.get("tech_stack"))

    def __add__(self, other):
        # method that allows to get alpha programmer # For alpha programmer we need + any of devs skills . But better salary
        return self.salary_per_day + other.salary_per_day


class Recruiter(Employee):
    # class Recruiter is inherited from Employee
    def __init__(self, first_name, last_name, email, phone, hired_at, salary_per_day):
        super().__init__(first_name, last_name, email, phone)
        self.hired_at = hired_at
        self.salary_per_day = salary_per_day

    def work(self):
        # method work is redefined
        return super().work().replace(".", " and start hiring.")

    def __str__(self):
        # method __str__ is redefined
        return "I'm recruiter " + self.first_name + " " + self.last_name + "."

    def __lt__(self, other):
        # with this methods recruiters can be compared by the salaries
        return self.salary_per_day < other.salary_per_day

    def __gt__(self, other):
        return self.salary_per_day > other.salary_per_day

    def set_hired_this_month(self, n):
        # adding of hired_this_month field
        self.hired_this_month = n

    def get_hired_this_month(self):
        try:
            return "I hired " + str(self.hired_this_month) + " persons this month!"
        except:
            return "Nobody was hired this month!"


class Candidate:
    # in **data any additional information can be put
    def __init__(self, first_name, last_name, email, phone, main_skill):
        super().__init__(first_name, last_name, email, phone)
        self.main_skill = main_skill
# If you call work method will show you error

    def work(self):
        raise ValueError

    @classmethod
    def create_from_csv(cls, fp):
        input_file = csv
