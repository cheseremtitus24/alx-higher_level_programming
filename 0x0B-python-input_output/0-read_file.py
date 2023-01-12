#!/usr/bin/python3
"""
This module performs a file read
and outputs file contents to
stdout
"""


def read_file(filename=""):
    """
    This function reads all the
    contents of a file and outputs
    them to stdout
    """
    with open(filename) as f:
        print(f.read(), end="")
