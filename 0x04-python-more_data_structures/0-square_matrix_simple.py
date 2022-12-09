#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    #mcopy = [x[:] for x in matrix]
    mcopy = list()
    for item in matrix:
        mcopy.append(item.copy())
    #mcopy = matrix.copy()
    for i in range(len(mcopy)):
        for j in range(len(mcopy)):
            mcopy[i][j] *= mcopy[i][j]

    return mcopy
