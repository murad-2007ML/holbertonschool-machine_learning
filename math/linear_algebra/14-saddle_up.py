#!/usr/bin/env python3
""" performs matrix multiplication"""
import numpy as np


def np_matmul(mat1, mat2):
    """
    You can assume that mat1 and mat2 are numpy.ndarrays

    You are not allowed to use any loops or conditional statements

    You may use: import numpy as np

    You can assume that mat1 and mat2 are never empty
    """
    multiple = np.dot(mat1, mat2)
    return multiple
