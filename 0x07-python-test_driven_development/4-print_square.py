#!/usr/bin/python3
"""This module only outputs a square matrix
and raises a TypeError and ValueError
"""


def print_square(size):
    """Returns nothing but only outputs a string on success else
    raises and exception

    Args:
        param1 (int):The first parameter.

    Returns:
        None: The return value. only outputs a string to stdout

    Raises:
        TypeError: if parameter value is not an integer
        ValueError:if parameter value is less than 0
    """
    # checking to ensure that the parameter is an instance of (int)
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # checking that the size integer is >= 0
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(size):
        for y in range(size):
            print("#", end="")
        print()
