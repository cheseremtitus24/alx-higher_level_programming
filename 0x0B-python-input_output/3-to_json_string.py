#!/usr/bin/python3
import json

"""
This module performs serialization of
python objects as json representation
"""


def to_json_string(my_obj):
    """
    Function serializes a parameter object to json
    and returns its json representation
    """
    value = json.dumps(my_obj, sort_keys=True)
    return value
