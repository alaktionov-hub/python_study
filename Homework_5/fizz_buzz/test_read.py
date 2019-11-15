#!/usr/bin/env python3

import sys
filename = sys.argv[1]

# lets open file (option 'r')
f = open(filename, 'r')
# for line in f:  # read each line from file
#    li = line.split()
#    li = list(map(int, li))  # Map all from line
# print([	li[0], li[1]], li[2])  # just test how work print 1 and 2 element
# f.close()  # and allways better close file

# print("Be happy!!!")


def read_file(file_name):

    for line in file_name:  # read each line from file
        li = line.split()
        # li = list(map(int, li))  # Map all from line
        li = [int(x) for x in line.split()]
    # print(li)
    # return(int(li[0]), int(li[1]), int(li[2]))
    return li


test = read_file(f)
print(test)
