#!/usr/bin/python3
def no_c(my_string):
    rmchars = ['C', 'c']
    size = len(my_string)

    for i in range(size):
        if my_string[i] not in rmchars:
            print("{}".format(my_string[i]), end="")
