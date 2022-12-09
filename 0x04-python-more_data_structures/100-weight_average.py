#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    denominator = 0
    def mult(x): return x[0] * x[1]
    multed = [list(map(mult, my_list))]
    numerator = sum(multed[0])

    for pair in my_list:
        denominator += pair[1]

    return numerator / denominator
