#!/usr/bin/python3

def uniq_add(my_list=[]):
    myset = my_list[:]
    myset = set(myset)
    result = 0
    for num in myset:
        result += num
    return result
