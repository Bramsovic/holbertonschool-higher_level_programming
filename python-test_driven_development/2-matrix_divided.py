#!/usr/bin/python3
"""
Module 2-matrix_divided
This module provides a function,
`matrix_divided(matrix, div)`, which
divides all elements of a matrix by a given
number and returns a new matrix
with the results rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given number.
    Args:
    matrix (list of lists): A matrix (list of lists)
    containing integers or floats.
    div (int or float): The number by which to divide
    each element of the matrix.
    Returns:
        list of lists: A new matrix with all elements
        divided by `div`, rounded to 2 decimal places.
    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats,
                   or if rows of the matrix are not of the same size,
                   or if `div` is not a number.
        ZeroDivisionError: If `div` is zero.
    """
    col_len = len(matrix[0])
    err_1 = 'matrix must be a matrix (list of lists) of integers/floats'
    err_2 = 'Each row of the matrix must have the same size'

    for row in matrix:
        if len(row) != col_len:
            raise TypeError(err_2)
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError(err_1)

    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    return [
        [round(element / div, 2) for element in row]
        for row in matrix
    ]
