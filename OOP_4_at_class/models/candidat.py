#!/usr/bin/env python3


class Candidat:
    def __init__(self, name, email, phone, technologies, main_skill, **data):
        self.name = name
        self.email = email
        self.phone = phone
        self.technologies = technologies
        self.main_skill = main_skill
        self.data = data
