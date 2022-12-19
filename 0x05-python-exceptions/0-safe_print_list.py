#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if !my_list:
        return (0)
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
        i = i + 1
    except BaseException:
        pass
    finally:
        if i:
            print()
        else:
            i = i - 1
        return (i)
