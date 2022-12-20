#!/usr/bin/python3
"""This is a Class with an instance private attribute called size"""
class Square:
    """This is a Class with an instance private attribute called size"""

    def __init__(self, size=0, position=(0, 0)):
        """ Initialization method for private attribute size and position"""
        self.__size = size
        self.__position = position

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

    def my_print(self):
        """ prints a # filled square to stdout"""
        if self.__size == 0:
            print()
        else:
            for x in range(self.__size):
                for y in range(self.__size):
                    print("#", end="")
                print()

    @property
    def position(self):
        """ Sets and gets the value of the private attribute position """
        return (self.__position)

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) == 2 and isdigit(
                value[0]) and isdigit(value[-1]):
            if value[0] < 0 or value[-1] < 0:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
            else:
                self.__size = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
