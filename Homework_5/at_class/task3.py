#!/usr/bin/env python3
# Read a text file and calculate frequency of words in it
import random
import re
import sys


def lower_fun(line):
    new_line = line.lower()
    return new_line


sample_file = open("example.txt", 'r')

words = sample_file.read().split()

my_final_list = [lower_fun(word) for word in words]

my_count = ({b: my_final_list.count(b.lower()) for b in (my_final_list)})

print(my_count)
