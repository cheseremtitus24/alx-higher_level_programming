#!/usr/bin/python3

def complex_delete(a_dictionary, value=""):

    # if value exists delete all key:value entries
    keys_list = list()

    for k, v in a_dictionary.items():
        if v == value:
            keys_list.append(k)
    for k in keys_list:
        del (a_dictionary[k])
    return a_dictionary
