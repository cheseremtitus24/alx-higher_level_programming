#!/usr/bin/python3
"""This module only outputs a persons name
and raises a TypeError when either the 
first or last name is not an instance of a string
"""


def say_my_name(first_name, last_name=""):
    """Returns nothing but only outputs a string on success else
    raises and exception

    Args:
        param1 (str):The first parameter.
        param2 (str): The second parameter.

    Returns:
        string: The return value. String for success, None otherwise.

    Raises:
        TypeError: if parameter values are neither a string
    """
    # checking to ensure that  either of the parameters is an instance of (str)

    a_list = (first_name, last_name)

    for x in a_list:
        if type(x) not in [str]:
            raise TypeError(
                "{} must be a string".format(
                    "first_name" if a_list.index(x) == 0 else "last_name"))
    # output the provided names
    print("My name is {:s} {:s}".format(first_name, last_name))
