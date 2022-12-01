#!/usr/bin/python3
from calculator_1 import add, mul, div, sub

if __name__ == '__main__':
    a = 10
    b = 5

    add = add(a, b)
    minus = sub(a, b)
    mult = mul(a, b)
    div = div(a, b)

    result = [add, minus, mult, div]
    operators = "+-*/"

    for index, val in enumerate(result):
        print(
            "{a} {op} {b} = {res}".format(
                a=a,
                op=operators[index],
                b=b,
                res=val))
