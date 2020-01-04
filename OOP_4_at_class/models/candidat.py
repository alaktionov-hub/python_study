#!/usr/bin/env python3


class Candidat:
    def __init__(self, name, email, phone, technologies, main_skill, **data):
        self.name = name
        self.email = email
        self.phone = phone
        self.technologies = technologies
        self.main_skill = main_skill
        self.data = data

    def validate(self, mail):
        print(self.get_emails_from_file())
        if mail in self.get_emails_from_file():
            raise ValueError

    def save_email_to_file(self):
        with open('emails', 'a') as file:
            file.write(self.email)
            file.write('\n')

    def get_emails_from_file(self):
        with open('emails', 'a+') as file:
            file.seek(0)
            data = file.read()
            return data.split('\n')
