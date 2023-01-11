#!/usr/bin/python3
def append_write(filename="", text=""):
    """
    This function append writes all the
    contents of an input text to a file
    and returns the number of characters written to the file
    """
    with open(filename, mode="a", "utf-8") as f:
        return f.write(text)
