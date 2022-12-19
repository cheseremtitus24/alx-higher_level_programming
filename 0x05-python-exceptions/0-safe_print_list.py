#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
        i = i + 1
    except BaseException:
        pass
    else:
        pass
    finally:
        if i:
            print()
        return (i)
