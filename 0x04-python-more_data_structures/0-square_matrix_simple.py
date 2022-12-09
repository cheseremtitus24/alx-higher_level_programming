#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if not matrix:
        return matrix

    def square(x): return x**2
    squared = [list(map(square, sublist)) for sublist in matrix]

    return squared
