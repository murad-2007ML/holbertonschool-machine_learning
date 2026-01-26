#!/usr/bin/env python3
"""concatenates two matrices along a specific axis"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    You can assume that mat1 and mat2 are 2D matrices containing ints/floats

    You can assume all elements in the same dimension are of the same type/shape

    You must return a new matrix

    If the two matrices cannot be concatenated, return None
    """
    if (len(mat1[0]) == len(mat2[0])) and axis == 0:
        new_mat1 = [i[:] for i in mat1]
        new_mat2 = [i[:] for i in mat2]
        return new_mat1 + new_mat2
    elif (len(mat1) == len(mat2)) and axis == 1:
        new_matrix = [mat1[i] + mat2[i] for i in range(len(mat1))]
        return new_matrix
    return None
