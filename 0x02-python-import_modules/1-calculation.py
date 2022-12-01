#!/usr/bin/python3
import calculator_1 as calc

if __name__ == '__main__':
    a = 10
    b = 5

    add = calc.add(a, b)
    minus = calc.sub(a, b)
    mult = calc.mul(a, b)
    div = calc.div(a, b)

    result = [add, minus, mult, div]
    operators = "+-*/"

    for index, val in enumerate(result):
        print(
            "{a} {op} {b} = {res}".format(
                a=a,
                op=operators[index],
                b=b,
                res=val))
