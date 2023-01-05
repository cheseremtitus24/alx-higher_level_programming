#!/usr/bin/python3
"""
This module defines a rectangle parent class
that has instance methods for data encapsulation using
the @property decorator function.

"""


class Rectangle:
    """ This is an that enables
    for the setting of a quadrilaterals
    height and width
    it further performs the computation of
    both area and perimeter
    """

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        """Width getter method returns a private object
        that is immutable
        Width setter:
            enables for the setting of width
            """
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) not in [int]:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """height getter method returns a private object
        that is immutable
        height setter:
        height setter:
            enables for the setting of height
            """
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) not in [int]:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """ Performs computation of the area of
        a quadrilateral and returns the area"""
        return self.width * self.height

    def perimeter(self):
        """ Performs computation of the perimeter of
        a quadrilateral and returns a perimeter"""
        return (2 * self.width) + (2 * self.height)
