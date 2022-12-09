#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    def square(x): return x**2
    return [list(map(square, sublist)) for sublist in matrix]
