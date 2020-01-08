#!/usr/bin/env python3


def check_emails(*emails):
    # for one_mail in emails:
    return len(set(emails)) == len(list(emails))


# print("a")
#check_emails('a@m.com', 'a@m.com', 'c@g.com')
# print("b")
#check_emails('a@m.com', 'c@m.com', 'c@g.com')
