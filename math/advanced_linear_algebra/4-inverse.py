#!/usr/bin/env python3
"""
Matrisin tərsini (inverse) hesablamaq üçün modul
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


def inverse(matrix):
    """
    Matrisin tərsini hesablayır.
    Matris sinqulyardırsa (det=0), None qaytarır.
    """
    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    if len(matrix) == 0 or any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    # Determinantı hesablayırıq
    det = determinant(matrix)
    if det == 0:
        return None

    n = len(matrix)
    if n == 1:
        return [[1 / matrix[0][0]]]

    # Adjugate (Kofaktorun transponirəsi) hesablanır
    inverse_matrix = []
    # Qeyd: Transponirəni birbaşa burada edirik
    for r in range(n):
        inv_row = []
        for c in range(n):
            # Kofaktor[c][r] üçün orijinal matrisdən c sətri və r sütunu silinir
            sub_matrix = [row[:r] + row[r+1:] for i, row in
                          enumerate(matrix) if i != c]

            minor_val = determinant(sub_matrix)
            sign = (-1) ** (c + r)

            # Tərs matris elementi = (1/det) * adjugate_element
            val = (sign * minor_val) / det
            inv_row.append(val)
        inverse_matrix.append(inv_row)

    return inverse_matrix