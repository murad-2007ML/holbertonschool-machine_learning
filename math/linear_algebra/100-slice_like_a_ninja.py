#!/usr/bin/env python3
"""slices a matrix along specific axes"""
import numpy as np


def np_slice(matrix, axes={}):
    """
    You can assume that matrix is a numpy.ndarray

    You must return a new numpy.ndarray

    axes is a dictionary where the key is an axis to slice along and the value is a tuple representing the slice to make along that axis

    You can assume that axes represents a valid slice
    """
    slices = slice(None) * matrix.ndim
    for axis, slice_args in axes.items():
        slices[axis] = slice(*slice_args)

    return matrix[tuple(slices)]
