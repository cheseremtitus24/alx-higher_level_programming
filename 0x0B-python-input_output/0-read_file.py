#!/usr/bin/python3
def read_file(filename=""):
    """
    This function reads all the
    contents of a file and outputs
    them to stdout
    """
    with open(filename) as f:
        print(f.read(), end="")
