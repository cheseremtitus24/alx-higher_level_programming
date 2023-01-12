#!/usr/bin/python3
import json

"""
This module contains a function that
reads a json string and loads it up
to memory as a python object
"""


def from_json_string(my_obj):
    """
    Function serializes a parameter object to json
    and returns its json representation
    """
    return json.loads(my_obj)
