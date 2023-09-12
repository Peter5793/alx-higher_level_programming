#!/usr/bin/python
"""
divides all the elemets in a matrix
"""
def matrix_divided(matrix, div):
    """
    divides all the elements in a matrix
    """
    size = None
    if type(matrix) is not list:
        raise TypeError (
            'matrix must be a matrix (list of lists) of integers/floats'
        )
    for row in matrix:
        if type(row) is not list:
            raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats'
            )
        if size is None:
            size = len(row)
        elif size != len(row):
            raise TypeError(
                'Each row of the matrix must be the same size'
            )
        for col in row:
            if not isinstance(col, int) and not isinstance(col, float):
                raise TypeError("matrix must be a matrix (list of lists) of integer/floats"
                                )
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError ('div must be a number')
    elif div == 0:
        raise ZeroDivisionError('division by zero')
    return [[round(col/div, 2) for col in row] for row in matrix]
