#!/usr/bin/python3

"""
This Module check to verify that the
parameter objects is a subclass of class
and returns True
else returns False
"""


def inherits_from(obj, a_class):
    """is_kind_of_class takes in two parameters of a class and an
    object and checks to verify that the object is an instance
    of the class and returns True else False
    """
    if (issubclass(type(obj), a_class)) and type(obj) not in [a_class]:
        return True
    else:
        return False
