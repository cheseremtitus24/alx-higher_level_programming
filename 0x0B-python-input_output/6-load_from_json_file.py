#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """
    This function reads all the
    contents of a file containing a
    json string and returns a object from
    the parsing of the json string
    """
    jobj = None
    with open(filename) as f:
        jobj = json.loads(f.read())

    return jobj
