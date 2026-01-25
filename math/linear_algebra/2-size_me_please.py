#!/usr/bin/env python3
"""calculates the shape of a matrix"""


def matrix_shape(matrix):
    """
    You can assume all elements in the same dimension are of the same type/shape
    The shape should be returned as a list of integers
    """
    shape = []
    while type(matrix) is list:
        shape.append(len(matrix))
        if len(matrix) == 0:
            break
        matrix = matrix[0]
    return shape
