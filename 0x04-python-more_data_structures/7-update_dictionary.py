#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):

    # if key exists the value is replaced

    if key in a_dictionary.keys():
        a_dictionary[key] = value
    else:
        # creating a new dictionary item
        a_dictionary[key] = value
    return a_dictionary
