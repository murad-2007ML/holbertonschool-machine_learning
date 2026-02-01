  GNU nano 6.2                                                                                                          102-squashed_like_sardines.py *                                                                                                                  
#!/usr/bin/env python3""" defines function that concatenates two matrices along a specific axis """


def matrix_shape(matrix):
    """ returns list of integers representing dimensions of given matrix """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        if len(matrix) == 0:
            break
        matrix = matrix[0]
    return shape


def cat_matrices(mat1, mat2, axis=0):
    """ concatenates two matrices along a specific axis """
    shape1 = matrix_shape(mat1)
    shape2 = matrix_shape(mat2)

    # Validate that matrices have the same number of dimensions
    if len(shape1) != len(shape2):
        return None

    # Validate all dimensions match EXCEPT for the concatenation axis
    for i in range(len(shape1)):
        if i != axis:
            if shape1[i] != shape2[i]:
                return None

    # Base Case: We've reached the target axis
    if axis == 0:
        # Create a new list combining elements of both matrices
        return mat1 + mat2

    # Recursive Step: Dive deeper into the nested lists
    # We decrement the axis so that the next call knows it's closer to the target
    new_matrix = []
    for i in range(len(mat1)):
        result = cat_matrices(mat1[i], mat2[i], axis - 1)
        if result is None:
            return None
        new_matrix.append(result)

    return new_matrix
