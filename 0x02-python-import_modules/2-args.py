#!/usr/bin/python3
import sys

if __name__ == '__main__':
    argc = len(sys.argv)
    print("{} arguments".format(argc - 1))
    for i in range(argc):
        if (argc == 1):
            continue
        print("{}: {}".format(i, sys.argv[i]))
