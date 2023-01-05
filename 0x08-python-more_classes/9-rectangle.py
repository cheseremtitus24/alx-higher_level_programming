#!/usr/bin/python3
"""
This module defines a rectangle parent class
that has instance methods for data encapsulation using
the @property decorator function.

"""


class Rectangle:
    """ This is an empty class """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        self.__class__.number_of_instances += 1

    @property
    def width(self):
        """Width getter method
        returns a private
        object that is immutable
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
        """Height getter method
        returns a private
        object that is
        immutable
        Height setter: """
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
                string += Rectangle.print_symbol
            string += "\n"
        return string[:-1]

    def __repr__(self):
        return f'Rectangle({self.width},{self.height})'

    def __del__(self):
        self.__class__.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ this method returns the biggest rectangle based on the area"""
        # Checking to ensure objects are instances of Rectangle class
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        This class method returns an equal sided quadrilateral
        """
        cls.width = cls.height = size
        return Rectangle(cls.width, cls.height)
