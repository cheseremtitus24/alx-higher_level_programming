#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    def square(x): return x**2
    return [list(map(lambda x:x**2, sublist)) for sublist in matrix]
