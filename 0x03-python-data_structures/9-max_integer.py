#!/usr/bin/python3
def max_integer(my_list=[]):

    # If list is empty return None
    if not my_list:
        return None

    max_val = 0

    for num in my_list:
        if num > max_val:
            max_val = num

    return max_val
