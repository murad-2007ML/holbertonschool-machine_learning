#!/usr/bin/env python3
"""
Minor matrisini hesablamaq üçün modulu ehtiva edir
"""


def determinant(matrix):
    """
    Matrisin determinantını rekursiv hesablayır
    """
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for c in range(n):
        # Birinci sətir üzrə alt matris yaradırıq
        sub_matrix = [row[:c] + row[c+1:] for row in matrix[1:]]
        det += ((-1) ** c) * matrix[0][c] * determinant(sub_matrix)
    return det


def minor(matrix):
    """
    Matrisin minor matrisini hesablayır
    """
    # Matrisin siyahıdan ibarət siyahı olmasını yoxlayırıq
    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    # Matrisin boş olmamasını yoxlayırıq
    if len(matrix) == 0:
        raise ValueError("matrix must be a non-empty square matrix")

    # Matrisin kvadrat olmasını yoxlayırıq
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    # 1x1 matris üçün xüsusi hal
    if n == 1:
        return [[1]]

    minor_matrix = []
    for r in range(n):
        row_minors = []
        for c in range(n):
            # Cari 'r' sətri və 'c' sütununu çıxararaq alt matris yaradırıq
            sub_matrix = [row[:c] + row[c+1:] for i, row in
                          enumerate(matrix) if i != r]
            # Alt matrisin determinantını hesablayırıq
            det = determinant(sub_matrix)
            row_minors.append(det)
        minor_matrix.append(row_minors)
    return minor_matrix
