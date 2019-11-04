#!/usr/bin/env python3
print ("This fizz-buzz task written on python")
line_print = ("------------------------------------------------------------")
print (line_print)

fizz = int(input("Please input fizz value: "))
print (line_print)

buzz = int(input("Please input buzz value: "))
print (line_print)

third_number = int(input("Please input third_number value: "))
print (line_print)

print ("SO What we have:" "\n" "Fizz =", fizz,"\n" "Buzz =", buzz,"\n" "third_number =", third_number, "\n") 

print ("Here is our answer: \n")
print (line_print)

#Start Calculate from 1
i = 1

#Please Note we will use print with extra options allow all be onb same line how it was on example
#Python 3 provides the simplest solution, all you have to do is to provide one extra argument to the print function. 
#You can use the optional named argument end to explicitly mention the string that should be appended at the end of the line.
#Whatever you provide as the end argument is going to be the terminating string.
#So if you provide an empty string, then no newline characters, and no spaces will be appended to your input.

#While i less then our third_number + 1 we work in 
while i < (third_number+1):
  if i%fizz == 0 and i%buzz == 0:  # If i multiple to fizz and buzz at same time print FB
    print("FB", end = ' ',) 
  elif i%fizz == 0:  # If i multiple to fizz only print F
    print("F", end = ' ',) 
  elif i%buzz == 0:  # If i multiple to buzz only print B
    print("B", end = ' ',)
  else:   # If i do not multiple to any checks before that print this value
    print (i, end = ' ',)
  i+=1 # i + 1 starting from 1 . And wait bevore i will be < that third_number what we input from keyboard

print ("\n")
print (line_print)
print ("\n Done!!!")