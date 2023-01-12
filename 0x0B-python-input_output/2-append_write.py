#!/usr/bin/python3
"""
This module contains a file write
method that utilizes the use of a
context manager
"""


def append_write(filename="", text=""):
    """
    This function append writes all the
    contents of an input text to a file
    and returns the number of characters written to the file
    """
    with open(filename, mode="w", "utf-8"):
        pass

    with open(filename, mode="a", "utf-8") as f:
        return f.write(text)
