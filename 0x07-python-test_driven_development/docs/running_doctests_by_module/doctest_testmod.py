def my_function(a, b):
    """Returns multiplication of strings and integers
    >>> my_function(2, 3)#doctest: +REPORT_NDIFF +NORMALIZE_WHITESPACE
    6 
    >>> my_function('a', 3) 
    'aaa'
    """
    return a * b

if __name__ == '__main__':
    import doctest
    doctest.testmod()
