#!/usr/bin/python3
import json


def from_json_string(my_obj):
    """
    Function serializes a parameter object to json
    and returns its json representation
    """
    return json.loads(my_obj)
