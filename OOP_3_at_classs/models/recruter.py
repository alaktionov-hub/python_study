#!/usr/bin/env python3


class Recruter(Employee):
    def work(self):
        return super().work().replace(".", "and I can find some people who will work for us")

    def __str__(self):
        return "Hello, my name is " + self.name + " " + "And my mail " + self.email + "And you can call me " + self.phone + " and I work here on postition Recruter"

    def __lt__(self, other):
        return self.day_salary < other.day_salary
