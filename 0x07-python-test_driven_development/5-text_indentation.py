#!/usr/bin/python3
"""This module parses input text and
performs substitution when special
characters are encountered from within the input string
and raises a TypeError when input is not a string
"""


def text_indentation(text):
    """Outputs additional 2 new lines when
    a period,comma,question mark or a full colon is
    encountered.


    Args:
        param1 (str):The first parameter.

    Returns:
        None: The return value. only outputs a string to stdout

    Raises:
        TypeError: if parameter value is not a string
    """
    # check whether the parameter input is a string

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_chars = ['.', '?', ':']

    # iterate through the input string performing substitution
    it = iter(text)
    sub = "\n\n"
    result = list()
    for char in it:
        if char in special_chars:
            result.append(char + sub)
        else:
            result.append(char)
    result = "".join(result)
    print(result, end="")
