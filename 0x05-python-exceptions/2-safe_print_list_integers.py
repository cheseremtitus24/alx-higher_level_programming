#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    temp_val = None
    for i in range(x):
        temp_val = my_list[i]
        if isinstance(temp_val, int):
            print("{:d}".format(temp_val), end="")
            i = i + 1

    if i:
        print()
    else:
        i = i - 1
    return (i)
