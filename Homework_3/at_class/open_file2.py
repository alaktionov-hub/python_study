#!/usr/bin/env python3

import sys
filename = sys.argv[1]

# дlets open file (option 'r')
f = open(filename, 'r')
for line in f:  # read each line from file
    print(line)  # Print this line
    li = line.split()
    print(li)
    li = list(map(int, li))
    print(li)
f.close()  # and allways better close file

print("Be happy!!!")
