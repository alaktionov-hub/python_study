#!/usr/bin/env python3


def fix_emails(*people):
    emails = []
    for one_man in people:
        emails.append(one_man.email)
    if len(emails) > len(set(emails)):
        raise ValueError
# print("a")
# check_emails('a@m.com', 'a@m.com', 'c@g.com')
# print("b")
# check_emails('a@m.com', 'c@m.com', 'c@g.com')
