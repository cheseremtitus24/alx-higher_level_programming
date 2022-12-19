#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            counter = counter + 1
    except BaseException:
        pass
    finally:
        if my_list:
            print()
        else:
            counter = 0
        return (counter)
