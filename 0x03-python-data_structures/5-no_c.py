#!/usr/bin/python3
def no_c(my_string):
    rmchars = ['C', 'c']
    for char in my_string:
        if char not in rmchars:
            print("{:s}".format(char), end="")
