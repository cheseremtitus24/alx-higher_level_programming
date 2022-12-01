#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)#!/usr/bin/python3

if __name__ == '__main__':
    a = 1
    b = 2
    print("{a} + {b} = {c}".format(a = a, b = b, c = add(a, b)))
