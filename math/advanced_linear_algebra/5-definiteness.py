#!/usr/bin/env python3
"""
Matrisin müəyyənliyini (definiteness) hesablamaq üçün modul
"""
import numpy as np


def definiteness(matrix):
    """
    Matrisin müəyyənliyini hesablayır.
    Kvadrat və simmetrik olmayan matrislər üçün None qaytarır.
    """
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")

    # Kvadrat və boş olub-olmamasını yoxlayırıq
    if matrix.size == 0 or matrix.ndim != 2 or \
       matrix.shape[0] != matrix.shape[1]:
        return None

    # Simmetriklik yoxlanışı (A == A.T)
    if not np.allclose(matrix, matrix.T):
        return None

    # Məxsusi ədədləri (eigenvalues) hesablayırıq
    try:
        eigenvalues = np.linalg.eigvals(matrix)
    except Exception:
        return None

    # Məxsusi ədədlərin işarələrini yoxlayırıq
    all_positive = np.all(eigenvalues > 0)
    all_negative = np.all(eigenvalues < 0)
    all_non_negative = np.all(eigenvalues >= 0)
    all_non_positive = np.all(eigenvalues <= 0)

    if all_positive:
        return "Positive definite"
    elif all_negative:
        return "Negative definite"
    elif all_non_negative:
        return "Positive semi-definite"
    elif all_non_positive:
        return "Negative semi-definite"
    else:
        return "Indefinite"
