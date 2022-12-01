#!/usr/bin/python3
import sys

if __name__ == '__main__':
    argc = len(sys.argv)
    if (argc == 1):
        print("{} arguments.".format(argc - 1))
    else:
        if argc == 2:
            print("{} argument:".format(argc - 1))
        else:
            print("{} arguments:".format(argc - 1))
        for i in range(argc):
            if i == 0:
                continue
            print("{}: {}".format(i, sys.argv[i]))
