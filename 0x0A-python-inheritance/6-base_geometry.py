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
