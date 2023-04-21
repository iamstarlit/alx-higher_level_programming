#!/usr/bin/python3
"""
2-matrix_divided.py

This module defines a function that divides
all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a `matrix` by `div`.

    This function divides all elements of a matrix by
    a given number, `div`.

    Args:
        matrix (List[List[Union[int, float]]]): a matrix
        div (int, float): Number to use to divide elements of `matrix`

    Raises:
        TypeError: If `matrix` contains NaN values
        TypeError: If `matrix` contains rows of different sizes
        TypeError: If `div` is not an int or float
        ZeroDivisionError: If `div` is 0

    Returns:
        A new divided matrix
    """

    # Check that `div` is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check that `div` is not 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Check that `matrix` is a list of lists of numbers
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(num, (int, float)) for row in matrix
                    for num in row)):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")

    # Check that all rows in the `matrix` have the same length
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Create a new matrix where each element is the result of dividing
    # the corresponding element of the original `matrix` by `div`
    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
