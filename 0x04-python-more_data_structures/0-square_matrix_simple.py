#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if not matrix:
        return matrix
    mcopy = list()
    for item in matrix:
        mcopy.append(item.copy())
    for i in range(len(mcopy)):
        for j in range(len(mcopy)):
            mcopy[i][j] *= mcopy[i][j]

    return mcopy
