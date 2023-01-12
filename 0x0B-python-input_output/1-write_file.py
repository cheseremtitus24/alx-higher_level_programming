#!/usr/bin/python3
"""
This module performs writing to files
making of the with context manager
"""


def write_file(filename="", text=""):
    """
    This function writes all the
    contents of an input text to a file
    and returns the number of characters written to the file
    """
    with open(filename, mode="w", "utf-8") as f:
        return f.write(text)
