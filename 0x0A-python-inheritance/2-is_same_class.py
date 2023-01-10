#!/usr/bin/python3

"""
This Module check to verify that the
parameter objects belong to the same class
else returns False
"""


def is_same_class(obj, a_class):
    """is_same_class take in two parameters of a class and an
    object and checks to verify that the object is an instance
    of the class and returns True else False
    """
    if (isinstance(obj, a_class)):
        return True
    else:
        return False
