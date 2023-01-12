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
    try:
        with open(filename, mode="a", encoding="utf-8") as f:
            return f.write(text)
    except BaseException:
        with open(filename, mode="w", encoding="utf-8"):
            return f.write(text)
