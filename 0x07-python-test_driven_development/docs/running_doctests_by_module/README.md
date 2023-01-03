The 6 has a trailing whitespace as shown by the output below
$cat doctest_testmod.py | cat -e
def my_function(a, b):$
    """Returns multiplication of strings and integers$
    >>> my_function(2, 3)#doctest: +REPORT_NDIFF +NORMALIZE_WHITESPACE$
    6 $
    >>> my_function('a', 3) $
    'aaa'$
    """$
    return a * b$
$
if __name__ == '__main__':$
    import doctest$
    doctest.testmod()$

# The Normalize whitespace allows for it to pass the tests


## Unittest Suite

When both unittest and doctest are used for testing the same code in different situations, the unittest integration in doctest can be used to run the tests together. 

Two classes,

**DocTestSuite & DocFileSuite**
create test suites compatible with the test-runner API of unittest.



