#!/usr/bin/python3

"""
This Module inherits from the list class and
adds a sorting algorithm to it
In this case we'll make use of merge sort
"""


def mergeSort(array):
    """ merge_sort is a modifier function
    that sorts the original list as it is
    passed by reference
    sourced from https://www.programiz.com/dsa/merge-sort
    """
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array) // 2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1


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
        #verify that the input values are all ints
        if (all(isinstance(x,int) for x in self)):
            l_copy = self.copy()
            mergeSort(l_copy)
            print(l_copy)
        else:
            raise TypeError("All List items must be integers")

