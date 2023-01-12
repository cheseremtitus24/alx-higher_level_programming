#!/usr/bin/python3
import json

"""
This Module performs saving of json data
to a file
"""


def save_to_json_file(my_obj, filename):
    """
    This function writes json dump contents to a file
    and returns the number of characters written to the file
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(json.dumps(my_obj))
