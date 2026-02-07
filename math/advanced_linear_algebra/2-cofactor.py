#!/usr/bin/env python3
"""
Kofaktor matrisini hesablamaq üçün modul
"""


def determinant(matrix):
    """Matrisin determinantını rekursiv hesablayır."""
    n = len(matrix)
    if n == 1:
        return matrix[0][0]

    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for c in range(n):
        sub_matrix = [row[:c] + row[c+1:] for row in matrix[1:]]
        det += ((-1) ** c) * matrix[0][c] * determinant(sub_matrix)
    return det


def cofactor(matrix):
    """
    Matrisin kofaktor matrisini hesablayır.
    """
    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    if len(matrix) == 0 or any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    n = len(matrix)
    if n == 1:
        return [[1]]

    cofactor_matrix = []

    for r in range(n):
        cofactor_row = []
        for c in range(n):
            # Minor üçün alt matris yaradırıq
            sub_matrix = [row[:c] + row[c+1:] for i, row in
                          enumerate(matrix) if i != r]

            # Minoru hesablayırıq
            minor_val = determinant(sub_matrix)

            # Şahmat qaydası ilə işarəni təyin edirik: (-1)^(r+c)
            sign = (-1) ** (r + c)
            cofactor_row.append(sign * minor_val)
        cofactor_matrix.append(cofactor_row)

    return cofactor_matrix
