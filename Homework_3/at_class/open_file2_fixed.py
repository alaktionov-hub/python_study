#!/usr/bin/env python3

import sys

# дlets open file (option 'r')
f = open(sys.argv[1], 'r')
for line in f:  # read each line from file
    li = [int(x) for x in line.split()]
    print(li)
f.close()  # and allways better close file

print("Be happy!!!")
