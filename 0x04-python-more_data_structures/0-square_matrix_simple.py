#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if not matrix:
        return matrix
    return [list(map(lambda x:x**2, sublist)) for sublist in matrix]

