#!/usr/bin/env python3
""" defines function that adds two matrices """


def matrix_shape(matrix):
    """ returns list of integers representing dimensions of given matrix """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        if len(matrix) == 0:
            break
        matrix = matrix[0]
    return shape


def add_matrices(mat1, mat2):
    """ returns new matrix that is sum of two matrices added element-wise """
    # Check if shapes are identical
    if matrix_shape(mat1) != matrix_shape(mat2):
        return None

    # Base case: if elements are not lists, they are numbers to be added
    if not isinstance(mat1, list):
        return mat1 + mat2

    # Recursive step: iterate through the lists and call add_matrices
    return [add_matrices(mat1[i], mat2[i]) for i in range(len(mat1))]
