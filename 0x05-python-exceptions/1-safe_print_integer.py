#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value), end="")
    except BaseException:
        return False
    else:
        print()
        return True
