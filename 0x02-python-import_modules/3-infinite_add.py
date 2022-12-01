#!/usr/bin/python3
import sys

if __name__ == '__main__':
    argc = len(sys.argv)
    result = 0
    for i in range(1, argc):
        result += int(sys.argv[i])

    print("{}".format(result))
