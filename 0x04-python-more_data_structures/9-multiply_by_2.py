#!/usr/bin/python3

def multiply_by_2(a_dictionary):

    # multiply every value in dictionary by 2
    copy_dict = dict()
    copy_dict = a_dictionary.copy()

    for k, v in copy_dict.items():
        copy_dict[k] *= 2
    return copy_dict
