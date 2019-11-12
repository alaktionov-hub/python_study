#!/usr/bin/env python3

import random
import re
import sys

f_text = open(sys.argv[1], 'r')
line_out = ""

for line in f_text:
    line_out += line
f_text.close()

slang_phrases = [", yeah!", ", this is crazy, I tell ya.", ", can U believe this?",
                 ", eh?", ", aw yea.", ", yo.", "? No way!", ". Awesome!"]

splited_string = re.findall(r'[^.!?]+', line_out)
print(splited_string)
f_text = open(sys.argv[2], 'w')
f_text.write((" ").join([str(x)+random.choice(slang_phrases)
                         for x in splited_string]))
f_text.close()
