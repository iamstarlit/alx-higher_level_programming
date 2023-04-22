#!/usr/bin/python3
"""
100-matrix_mul.py

This module contains a function to multiply two matrices.
"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices.

    Args:
        m_a (list): The first matrix
        m_b (list): The second matrix

    Raises:
        TypeError: If `m_a` or `m_b` is not a list.
        TypeError: If `m_a` or `m_b` is not a list of lists.
        TypeError: If `m_a` or `m_b` is empty.
        TypeError: If elements of `m_a` or `m_b`  are not integers or floats.
        TypeError: If the rows of `m_a` and `m_b` are not the same.
        ValueError: If `m_a` and `m_b` cannot be multplied.

    Returns:
        The result of multiplication.
    """

    # Check that `m_a`and `m_b` are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Check that `m_a` and `m_b` are lists of lists
    for elems in m_a:
        if not isinstance(elems, list):
            raise TypeError("m_a must be a list of lists")
    for elems in m_b:
        if not isinstance(elems, list):
            raise TypeError("m_b must be a list of lists")

    # Check that `m_a` and `m_b` are not empty
    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    # Check that the elements of `m_a` and `m_b` are integers or floats
    for lists in m_a:
        for elems in lists:
            if not isinstance(elems, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for lists in m_b:
        for elems in lists:
            if not isinstance(elems, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    # Check that the rows of `m_a` and `m_b` have the same size
    lenght = 0
    for elems in m_a:
        if lenght != 0 and lenght != len(elems):
            raise TypeError("each row of m_a must be of the same size")
        lenght = len(elems)
    lenght = 0
    for elems in m_b:
        if lenght != 0 and lenght != len(elems):
            raise TypeError("each row of m_b must be of the same size")
        lenght = len(elems)

    # Check that `m_a` and `m_b` can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Initialize the result matrix
    result = []
    for i in range(len(m_a)):
        result.append([0] * len(m_b[0]))

    # Perform the matrix multiplication
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
