#!/usr/bin/python3
def getfirstdigit(n):
    while n >= 10:
        n /= 10
    return n


def getlastdigit(n):
    return n % 10


for i in range(0, 99 + 1):
    if (i == 99):
        print("{}".format(str(i).zfill(2)))
        continue
    print("{}, ".format(str(i).zfill(2)), end="")
