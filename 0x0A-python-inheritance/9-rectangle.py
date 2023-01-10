#!/usr/bin/python3
"""
This Module contains a geometric class that
that contains a public class function
that raises an exception when called/invoked
"""


class BaseGeometry(object):
    """
    This is an empty class
    that does
    nothing
    """

    def area(self):
        """area is an unimplemented class
        function that raises a custom
        exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """area is an unimplemented class
        function that raises a custom
        exception"""
        # validating to ensure name is always a string
        if type(name) not in [str]:
            raise TypeError("{} must be a string".format(name))
        # validating to ensure value is always an integer
        if type(value) not in [int]:
            raise TypeError("{} must be an integer".format(name))

        # validating to ensure value is greater than 0
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle is a subclass
    and is a child of the BaseGeometry
    class"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ This function computes the area of a rectangle
        by multiplying its width and height and returns
        the result
        """
        return self.__width * self.__height

    def __str__(self):
        """ str is a magic method that returns a pretty formatted
        string that is useful to end users """
        return "[{}] {}/{}".format(self.__class__.__name__,
                                   self.__width, self.__height)
