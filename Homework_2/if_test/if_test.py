#!/usr/bin/env python3
# Just if test
#
print("For registration, indicate your age?")
user_age = int(input("How old are you? :"))

if (user_age < 18):
    print("Are you sure your mom knows where you are?")
elif (user_age < 30):
    print("Hello new young user")
elif (user_age < 60):
    print("Hello new user")
else:
    print("Welcome")
