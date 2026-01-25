#!/usr/bin/env python3
"""Transpose of a matrix"""


def matrix_transpose(matrix):
    """
    You must return a new matrix
    You can assume that matrix is never empty
    You can assume all elements in the same dimension are of the
    same type/shape
    """
    new = []
    for i in range(len(matrix[0])):
        matrix_element = []
        for j in range(len(matrix)):
            matrix_element.append(matrix[j][i])
        new.append(matrix_element)
    return new
