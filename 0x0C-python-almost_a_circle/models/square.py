#!/usr/bin/python3
"""
This module contains the base class
of a set of inherited classes.
It is responsible for autogenerating the
unique id's of each created object
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ This class represent the base class
    and contains an initialization instance method
    that autogenerates instance number id's of
    class objects
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        This is an initialization instance method
        that autogenerates instance object's ids
        and takes in a single parameters that
        accept integers.
        It also takes in a default value of None
        """

        # Calling the base class init method and passing it
        # the value of id so that it can be initialized with
        # the instance methods defined in the base class
        self.__size = size
        self.__x = x
        self.__y = y
        self.__id = id

        super().__init__(self.__size, self.__size, self.__x, self.__y, self.__id)

        # property setter and getter methods for instance attributes

        # property setter and getter methods for instance attributes

    @property
    def size(self):
        """Get or set the value of the `size` property.

        Returns:
            int: The value of the `size` property.
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        Sets the value of size and
        validates to ensure that it is
        and integer value that is
        greater than or equal to zero
        """
        if type(size) in [int]:
            if size > 0:
                self.__size = size
                self.__width = size
                self.__height = size
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def x(self):
        """Get or set the value of the `x` property.

               Returns:
                   int: The value of the `x` property.
               """
        return self.__x

    @x.setter
    def x(self, x):
        """
        Sets the value of x and
        validates to ensure that it is
        and integer value that is
        greater than or equal to zero
        """
        if (type(x) in [int]):
            if (x >= 0):
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
        """
        Sets the value of y and
        validates to ensure that it is
        and integer value that is
        greater than or equal to zero
        """
        if (type(y) in [int]):
            if (y >= 0):
                self.__y = y
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")

    def __str__(self):
        """
        is a magic method that returns pretty formatted string
        that is of significance to user
        """
        formatted_string = "[{rect}] ({id:d}) {x:d}/{y:d} - {width:d}".format(
            rect=self.__class__.__name__,
            id=self.id,
            x=self.__x,
            y=self.__y,
            width=self._Rectangle__width)
        return formatted_string

    def update(self, *args, **kwargs):
        """Updates the values of instance attributes
        by expanding the *args and assigning
        the values to attributes based on indexes

        example:
        index 1 value saves to : id
        index 2 value saves to : width -> size
        index 2 value saves to : height -> size
        index 3 value saves to : x
        index 4 value saves to : y
                """
        for i in range(len(args)):
            if i == 0:
                # before setting perform a validation for type and value
                if type(args[i]) in [int]:
                    if args[i] >= 0:
                        self.id = args[i]
                    else:
                        raise ValueError("id must be >= 0")
                else:
                    raise TypeError("id must be an integer")

            elif i == 1:
                # before setting perform a validation for type and value
                if type(args[i]) in [int]:
                    if args[i] >= 0:
                        self.__size = args[i]
                        self._Rectangle__width = self.__size
                        self._Rectangle__height = self.__size
                    else:
                        raise ValueError("width must be >= 0")
                else:
                    raise TypeError("width must be an integer")
            elif i == 2:
                # before setting perform a validation for type and value
                if type(args[i]) in [int]:
                    if args[i] >= 0:
                        self.__x = args[i]
                    else:
                        raise ValueError("x must be >= 0")
                else:
                    raise TypeError("x must be an integer")

            elif i == 3:
                # before setting perform a validation for type and value
                if type(args[i]) in [int]:
                    if args[i] >= 0:
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

            elif key == "size":
                if type(value) in [int]:
                    if value >= 0:
                        self.__size = value
                        self._Rectangle__width = self.__size
                        self._Rectangle__height = self.__size
                    else:
                        raise ValueError("width must be >= 0")
                else:
                    raise TypeError("width must be an integer")

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle
        with all it's instance attributes

                    Returns:
                         dict: dictionary representation of the rectangle
                """
        square_obj = {
            'id': self.id,
            'x': self.__x,
            'size': self.__size,
            'y': self.__y}
        return square_obj
