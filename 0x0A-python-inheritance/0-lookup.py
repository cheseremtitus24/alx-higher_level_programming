#!/usr/bin/python3
"""
This Module contains a lookup function that
reports a list of methods and attributes of an
object
"""


def lookup(obj):
    """
    the dir function can be used to retrieve a
    list of object attributes and methods

    parameter1 object:
    returns a dir object representation of attributes and
    methods
    """
    return dir(obj)
