#!/usr/bin/python3

def best_score(a_dictionary):

    if a_dictionary is None:
        return None

    # returns the key with the highest key value

    max_val = 0
    max_key = None
    for k, v in a_dictionary.items():
        if v > max_val:
            max_val = v
            max_key = k
    return max_key
