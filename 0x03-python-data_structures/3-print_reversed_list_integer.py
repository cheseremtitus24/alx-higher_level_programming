#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    size = len(my_list)
    if size == 0:
        return my_list
    my_list.reverse()
    for i in range(size):
        print("{:d}".format(my_list[i]))
