#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    temp_val = None
    counter = 0
    try:
        for i in range(x):
            temp_val = my_list[i]
            if isinstance(temp_val, int):
                print("{:d}".format(temp_val), end="")
                counter = counter + 1
    except IndexError as e:
        print("\nIndexError: {}".format(e), end="")

    finally:

        if counter:
            print()
        return (counter)
