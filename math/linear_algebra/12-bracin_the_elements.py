#!/usr/bin/env python3
"""performs element-wise addition, subtraction, multiplication, and division"""


def np_elementwise(mat1, mat2):
    """
    Returns a tuple containing the element-wise sum, difference,
    product, and quotient of two matrices.
    """
    return mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2
