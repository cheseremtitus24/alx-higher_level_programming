#!/usr/bin/python3

"""
This Module inherits from the list class and
adds a sorting algorithm to it
In this case we'll make use of merge sort
"""


def merge_sort(list_to_sort):
    """ merge_sort is a perfect function
    that sorts a list are returns
    a sorted list
    """
    # Check for Verify input type to only be a list
    if type(list_to_sort) in [list]:
        l_local = list_to_sort.copy()
        # return sorted_list
        pass
    else:
        raise TypeError("{} must be a list".format(list_to_sort))


class MyList(list):
    """ MyList is a subclass of the list
    parent class and takes in an iterable as an
    optional parameter
    This class only adds a print function that
    outputs a sorted list to stdout
    """

    def print_sorted(self):
        """
        The print_sorted function only outputs
        a sorted list and does not modify the
        original input list and only makes a copy
        """
        l_copy = merge_sort(self)
        print(l_copy)
