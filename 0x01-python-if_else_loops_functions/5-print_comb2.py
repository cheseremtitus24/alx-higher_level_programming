#!/usr/bin/python3
def getfirstdigit(n):
    while n >= 10:
        n /= 10
    return n


def getlastdigit(n):
    return n % 10


for i in range(0, 99 + 1):
    if i > 0 and i < 10:
        print(f"{i:02d}, ", end="")
        continue
    if (i == 89):
        if (getfirstdigit(i) < getlastdigit(i)):
            print(f"{i:02d}")
            continue
    if (getfirstdigit(i) < getlastdigit(i)):
        print(f"{i:02d}, ", end="")
    continue
