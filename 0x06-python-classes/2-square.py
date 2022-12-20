#!/usr/bin/python3
"""This is a Class with an instance private attribute called size"""


class Square:
    """This is a Class with an instance private attribute called size"""

    def __init__(self, size=0):
        """ Initialization method for private attribute size"""
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
