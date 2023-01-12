#!/usr/bin/python3

import sys
""" This module
reads data from commandline arguments and saves
them to a list and then saved to the same file
as a json string
"""
if __name__ == "__main__":
    """ Function reads commandline args
    and saves them as json string to a file
    """

    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__(
        '6-load_from_json_file').load_from_json_file
    # print("This is the name of the script:", sys.argv[0])
    # print("Number of arguments:", len(sys.argv))
    # print("The arguments are:", str(sys.argv))
    # try to open file
    my_list_obj = list()
    try:
        # load data from file
        my_list_obj = load_from_json_file("add_item.json")
    except BaseException:
        # file not exist just write string to file
        save_to_json_file(sys.argv[1:], "add_item.json")
    else:
        # no errors encountered
        for item in sys.argv[1:]:
            my_list_obj.append(item)
        save_to_json_file(my_list_obj, "add_item.json")
