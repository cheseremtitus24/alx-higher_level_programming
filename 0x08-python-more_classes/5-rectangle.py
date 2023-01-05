#!/usr/bin/python3
"""
This module defines a rectangle parent class
that has instance methods for data encapsulation using
the @property decorator function.

"""


class Rectangle:
    """ This is an empty class """

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        """Width getter method returns a private object that is immutable
        Width setter: """
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) not in [int]:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @width.deleter
    def width(self):
        pass

    @property
    def height(self):
        """Width getter method returns a private object that is immutable
        Width setter: """
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) not in [int]:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @height.deleter
    def height(self):
        pass

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        string = ""
        for row in range(self.height):
            for column in range(self.width):
                string += "#"
            string += "\n"
        return string[:-1]

    def __repr__(self):
        return f'Rectangle({self.width},{self.height})'

    def __del__(self):
        print("Bye rectangle...")
