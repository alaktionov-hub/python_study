#!/usr/bin/env python3

import sys
filename = sys.argv[1]

# lets open file (option 'r')
f = open(filename, 'r')
for line in f:  # read each line from file
    print(line)  # Print this line
f.close()  # and allways better close file

print("Be happy!!!")
