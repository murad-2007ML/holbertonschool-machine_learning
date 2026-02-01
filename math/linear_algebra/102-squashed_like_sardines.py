#!/usr/bin/env python3
""" defines function that concatenates two matrices along a specific axis """


def matrix_shape(matrix):
    """ returns list of integers representing dimensions of given matrix """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        if len(matrix) == 0:
            break
        matrix = matrix[0]
    return shape


def cat_matrices(mat1, mat2, axis=0):
    """ concatenates two matrices along a specific axis """
    shape1 = matrix_shape(mat1)
    shape2 = matrix_shape(mat2)

    if len(shape1) != len(shape2):
        return None

    for i in range(len(shape1)):
        if i != axis and shape1[i] != shape2[i]:
            return None

    if axis == 0:
        return mat1 + mat2

    # Breaking the recursive call into a cleaner loop to avoid E501
    new_matrix = []
    for i in range(len(mat1)):
        res = cat_matrices(mat1[i], mat2[i], axis - 1)
        if res is None:
            return None
        new_matrix.append(res)

    return new_matrix
