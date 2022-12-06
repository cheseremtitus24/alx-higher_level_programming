#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    lst_len = len(my_list)
    list_copy = my_list.copy()

    for i in range(lst_len):
        if list_copy[i] % 2 == 0:
            list_copy[i] = True
        else:
            list_copy[i] = False

    return list_copy
