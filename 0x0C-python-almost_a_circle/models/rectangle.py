"""
This module contains the base class
of a set of inherited classes.
It is responsible for autogenerating the
unique id's of each created object
"""
from models.base import Base
import json


class Rectangle(Base):
    """ This class represent the base class
    and contains an initialization instance method
    that autogenerates instance number id's of
    class objects
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        This is an initialization instance method
        that autogenerates instance object's ids
        and takes in a single parameters that
        accept integers.
        It also takes in a default value of None
        """

        if (self.__validate_type_is_int(width)):
            if (self.__validate_value(width)):
                self.__width = width
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

        if (self.__validate_type_is_int(height)):
            if (self.__validate_value(height)):
                self.__height = height
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

        if (self.__validate_type_is_int(x)):
            if (self.__validate_value(x)):
                self.__x = x
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")

        if (self.__validate_type_is_int(y)):
            if (self.__validate_value(y)):
                self.__y = y
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("y must be an integer")
        # Calling the base class init method and passing it
        # the value of id so that it can be initialized with
        # the instance methods defined in the base class
        self.__id = id
        super().__init__(self.__id)

    def __validate_type_is_int(self, value):
        """check is the type of a value is an integer class

                    Args:
                         value (*): The value to be checked.

                    Returns:
                         bool: True if type of value is an int else False
                """
        if (type(value) in [int]):
            return True
        else:
            return False

    def __validate_value(self, value):
        """check is the type of a value is an integer class and
        is greater than or equal to zero

                    Args:
                         val (int): The value to be checked.

                    Returns:
                         bool: True if type of value is an int else False
                """
        if (value >= 0):
            return True

        return False

    # property setter and getter methods for instance attributes

    @property
    def width(self):
        """Get or set the value of the `width` property.

        Returns:
            int: The value of the `width` property.
        """
        return self.__width

    @width.setter
    def width(self, width):
        if (self.__validate_type_is_int(width)):
            if (self.__validate_value(width)):
                self.__width = width
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """Get or set the value of the `height` property.

               Returns:
                   int: The value of the `height` property.
               """
        return self.__height

    @height.setter
    def height(self, height):
        if (self.__validate_type_is_int(height)):
            if (self.__validate_value(height)):
                self.__height = height
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        """Get or set the value of the `x` property.

               Returns:
                   int: The value of the `x` property.
               """
        return self.__x

    @x.setter
    def x(self, x):
        if (self.__validate_type_is_int(x)):
            if (self.__validate_value(x)):
                self.__x = x
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")

        # check that value passed in is >= 0

    @property
    def y(self):
        """Get or set the value of the `y` property.

               Returns:
                   int: The value of the `y` property.
               """
        return self.__y

    @y.setter
    def y(self, y):
        if (self.__validate_type_is_int(y)):
            if (self.__validate_value(y)):
                self.__y = y
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")

    def area(self):
        """multiply height and weight of a quadrilateral

                    Args:
                         self.__width (int): The first number to multiply.
                         self.__height (int): The second number to multiply.

                    Returns:
                         int: The product of the width and height of a quadrilateral.
                """
        self.__result = self.__width * self.__height

        return self.__result

    def display(self):
        """
        display prints a matrix representation of the quadrilateral
        and fills it with '#' Character to form a filled 4 sided
        block
                """
        if (self.__y):
            for x in range(self.__y):
                print()
        for i in range(self.__height):
            if (self.__x):
                print(" " * self.__x, end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        is a magic method that returns pretty formatted string
        that is of significance to user
        """
        formatted_string = "[{rect}] ({id:d}) {x:d}/{y:d} - {width:d}/{height:d}".format(
            rect=self.__class__.__name__,
            id=self.id,
            x=self.__x,
            y=self.__y,
            width=self.__width,
            height=self.__height)
        return formatted_string

    def update(self, *args, **kwargs):
        """Updates the values of instance attributes
        by expanding the *args and assigning
        the values to attributes based on indexes

        example:
        index 1 value saves to : id
        index 2 value saves to : width
        index 3 value saves to : height
        index 4 value saves to : x
        index 5 value saves to : y
                """
        for i in range(len(args)):
            if i == 0:
                # before setting perform a validation for type and value
                if type(args[i]) in [int]:
                    if args[i] > 0:
                        self.id = args[i]
                    else:
                        raise ValueError("id must be >= 0")
                else:
                    raise TypeError("id must be an integer")

            elif i == 1:
                # before setting perform a validation for type and value
                if type(args[i]) in [int]:
                    if args[i] > 0:
                        self.__width = args[i]
                    else:
                        raise ValueError("width must be >= 0")
                else:
                    raise TypeError("width must be an integer")
            elif i == 2:
                # before setting perform a validation for type and value
                if type(args[i]) in [int]:
                    if args[i] > 0:
                        self.__height = args[i]
                    else:
                        raise ValueError("height must be >= 0")
                else:
                    raise TypeError("height must be an integer")

            elif i == 3:
                # before setting perform a validation for type and value
                if type(args[i]) in [int]:
                    if args[i] > 0:
                        self.__x = args[i]
                    else:
                        raise ValueError("x must be >= 0")
                else:
                    raise TypeError("x must be an integer")

            elif i == 4:
                # before setting perform a validation for type and value
                if type(args[i]) in [int]:
                    if args[i] > 0:
                        self.__y = args[i]
                    else:
                        raise ValueError("y must be >= 0")
                else:
                    raise TypeError("y must be an integer")

        # todo: validate value and type as did before
        for key, value in kwargs.items():
            if key == "id":
                if type(value) in [int]:
                    if value >= 0:
                        self.id = value
                    else:
                        raise ValueError("id must be >= 0")
                else:
                    raise TypeError("id must be an integer")
            elif key == "x":
                if type(value) in [int]:
                    if value >= 0:
                        self.__x = value
                    else:
                        raise ValueError("x must be >= 0")
                else:
                    raise TypeError("x must be an integer")
            elif key == "y":
                if type(value) in [int]:
                    if value >= 0:
                        self.__y = value
                    else:
                        raise ValueError("y must be >= 0")
                else:
                    raise TypeError("y must be an integer")

            elif key == "width":
                if type(value) in [int]:
                    if value >= 0:
                        self.__width = value
                    else:
                        raise ValueError("width must be >= 0")
                else:
                    raise TypeError("width must be an integer")
            elif key == "height":
                if type(value) in [int]:
                    if value >= 0:
                        self.__height = value
                    else:
                        raise ValueError("height must be >= 0")
                else:
                    raise TypeError("height must be an integer")

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle
        with all it's instance attributes

                    Returns:
                         dict: dictionary representation of the rectangle
                """
        rect = {
            'x': self.__x,
            'y': self.__y,
            'id': self.id,
            'height': self.__height,
            'width': self.__width}
        return rect
