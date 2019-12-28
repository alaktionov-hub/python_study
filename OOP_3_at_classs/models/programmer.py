#!/usr/bin/env python3


class Programmer(Employee):
    def work(self):
        return super().work().replace(".", "and I can CODE")

    def __str__(self):
        return "Hello, my name is " + self.name + " " + "And my mail " + self.email + "And you can call me " + self.phone + " and I work here on position Programmer"
# Need find way to fix for compare also salary not only tech stack

    def __lt__(self, other):
        return self.day_salary < other.day_salary

    def __gt__(self, other):
        return len(self.data.get("tech_stack")) > len(other.data.get("tech_stack"))

    def __lt__(self, other):
        return len(self.data.get("tech_stack")) < len(other.data.get("tech_stack"))

    def __eq__(self, other):
        return len(self.data.get("tech_stack")) == len(other.data.get("tech_stack"))
