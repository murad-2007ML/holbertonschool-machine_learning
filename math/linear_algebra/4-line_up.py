#!/usr/bin/env python3
"""adds two arrays element-wise"""


def add_arrays(arr1, arr2):
    """
    You can assume that arr1 and arr2 are lists of ints/floats

    You must return a new list

    If arr1 and arr2 are not the same shape, return None
    """
    if len(arr1) != len(arr2):
        return None
    new = []
    for i in range(len(arr1)):
        new.append(arr1[i] + arr2[i])
    return new
