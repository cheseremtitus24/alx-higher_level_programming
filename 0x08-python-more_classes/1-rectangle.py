"""
This module defines a rectangle parent class
that has instance methods for
data encapsulation using
the
@property decorator function.

"""


class Rectangle:
    """ This is a rectangle class
        that has encapsulation functions that
        get and set the width and height
        of a rectangle object

    """

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
       """ 
        Returns the summation of integers and floats

        Args:
         param1 (list(list(int:float),list(int:float),...):
         The first parameter.
         param2 (int:float): The second parameter.

        Returns:
         bool: The return value. True for success, False otherwise.

        Raises:
         TypeError: if list items are neither an int || float
         : if matrix element list are of different lengths
         ZeroDivisionError: if divisor equals to 0
         """
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
       """ 
        Returns the summation of integers and floats

        Args:
         param1 (list(list(int:float),list(int:float),...):
         The first parameter.
         param2 (int:float): The second parameter.

        Returns:
         bool: The return value. True for success, False otherwise.

        Raises:
         TypeError: if list items are neither an int || float
         : if matrix element list are of different lengths
         ZeroDivisionError: if divisor equals to 0
         """
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
