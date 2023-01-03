#!/usr/bin/python3
"""This module performs arithmetic operations
the matrix_divided performs arithmetic division and peforms
rounding to 2dp
"""

def matrix_divided(a, b):
    """Returns the summation of integers and floatsi

    Args:
        param1 (list(list(int:float),list(int:float),...): The first parameter.
        param2 (int:float): The second parameter.

    Returns:
        bool: The return value. True for success, False otherwise.

    Raises: 
        TypeError: if list items are neither an int || float
                 : if matrix element list are of different lengths
        ZeroDivisionError: if divisor equals to 0

    """
    # checking to ensure that the divisor is of instance (int,float)
    if type(b) not in [int,float]:
        raise TypeError("div must be a number")
    if b == 0:
        raise ZeroDivisionError('division by zero')

#    if not a or not isinstance(a,list) or isinstance(a[0],list):
#        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(a) not in [list]:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if type(a[0]) not in [list]:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")






    # testing that each row of matrix are of same length else raise exception
    # Iterate through the rows of matrix to check if all are of same length
    if not len(set(map(len,a)))==1:
        raise TypeError("Each row of the matrix must have the same size")

    # testing that matrix contains only a list of list of (ints &&,||floats)
    it = iter(a)
    for x in it:
        temp = iter(x)
        for y in temp:
            if type(y) not in [int,float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")


    # divide each and every element in matrix by a devidend number

    results = list()
    val = lambda x: float(format(x / b,".2f"))


    it = iter(a)
    for a_list in it:
        # perform division list-wise
        results.append(list(map(val,a_list)))


                
    return results

