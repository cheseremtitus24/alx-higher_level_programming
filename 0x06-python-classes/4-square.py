#!/usr/bin/python3
"""This is a Class with an instance private attribute called size"""
class Square:
    """This is a Class with an instance private attribute called size"""

    def __init__(self, size=0):
        """ Initialization method for private attribute size"""
        self.__size = size

    @property
    def size(self):
        """ Sets and gets the value of the private attribute size """
        return (self.__size)

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ Returns the area of a Square """
        return (self.__size ** 2)
