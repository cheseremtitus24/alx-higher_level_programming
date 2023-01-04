#!/usr/bin/python3
"""This module performs arithmetic operations
the add_integer perform arithmetic add and peforms
floor of the results so that it
does not return values that
have decimal places
"""


def add_integer(a, b=98):
    """Returns the summation of integers and floatsi

    Args:
        param1 (int:float): The first parameter.
        param2 (int:float): The second parameter.

    Returns:
        int: The return value. Integer value

    Raises: TypeError: if parameters are neither an int || float

    """

    # a and b must be integers or floats else raise TypeError
    v = [a, b]
    r = list()
    a_message = "a must be an integer"
    b_message = "b must be an integer"
    for i in range(2):
        temp = v[i]
        if isinstance(temp, int) or isinstance(temp, float):
            pass
        else:
            raise TypeError(a_message if i < 1 else b_message)

    # When execution reaches here that mean no exception was raised
    return int(a + b)
