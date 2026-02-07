#!/usr/bin/env python3

def determinant(matrix):
    """
    Helper function to calculate the determinant of a matrix recursively.
    """
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    for c in range(n):
        # Create submatrix for expansion along first row
        sub_matrix = [row[:c] + row[c+1:] for row in matrix[1:]]
        det += ((-1) ** c) * matrix[0][c] * determinant(sub_matrix)
        
    return det

def minor(matrix):
    """
    Calculates the minor matrix of a matrix.
    
    Args:
        matrix: A list of lists representing a square matrix.
        
    Returns:
        The minor matrix of the input matrix.
        
    Raises:
        TypeError: If matrix is not a list of lists.
        ValueError: If matrix is not square or is empty.
    """
    # Validate that matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    
    # Validate that matrix is not empty
    if len(matrix) == 0:
        raise ValueError("matrix must be a non-empty square matrix")
        
    # Validate that matrix is square (rows == cols for all rows)
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")
    
    # Edge case for 1x1 matrix
    # The minor of a 1x1 matrix element is the determinant of a 0x0 matrix, which is 1.
    if n == 1:
        return [[1]]
    
    minor_matrix = []
    
    for r in range(n):
        row_minors = []
        for c in range(n):
            # Create submatrix by removing the current row 'r' and column 'c'
            sub_matrix = [row[:c] + row[c+1:] for i, row in enumerate(matrix) if i != r]
            
            # Calculate the determinant of the submatrix
            det = determinant(sub_matrix)
            row_minors.append(det)
        minor_matrix.append(row_minors)
        
    return minor_matrix