#!/usr/bin/env python3
"""performs matrix multiplication"""


def mat_mul(mat1, mat2):
    """
    You can assume that mat1 and mat2 are 2D matrices containing ints/floats

    You can assume all elements in the same dimension are of the same type/shape

    You must return a new matrix

    If the two matrices cannot be multiplied, return None
    """
    if len(mat1[0]) != len(mat2):
        return None
    else:
        new_mat = []
        for i in range(len(mat1)):
            mat_i = []
            for j in range(len(mat2[0])):
                vec = 0
                for k in range(len(mat2)):
                    vec += mat1[i][k] * mat2[k][j]
                mat_i.append(vec)
            new_mat.append(mat_i)
        for x in new_mat:
            return new_mat
