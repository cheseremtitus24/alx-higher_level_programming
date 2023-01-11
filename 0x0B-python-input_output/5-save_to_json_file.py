#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    """
    This function writes json dump contents to a file
    and returns the number of characters written to the file
    """
    with open(filename, mode="w", "utf-8") as f:
        return f.write(json.dumps(my_obj))
