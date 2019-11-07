#!/usr/bin/env python3

import sys
filename = sys.argv[1]

# lets open file (option 'r')
f = open(filename, 'r')
for line in f:  # read each line from file
    print(line)  # Print this line
    li = line.split()
    print(li)
    li = list(map(int, li))  # Map all from line
    print(li)
    print([	li[0], li[1]])  # just test how work print 1 and 2 element
f.close()  # and allways better close file

print("Be happy!!!")
