#!/usr/bin/python3
"""
12-pascal_triangle.py

Defines a function that returns a Pascal's triangle of n:
"""


def pascal_triangle(n):
    """Return Pascal's triangle of size n.

    Args:
        n (int): number of rows of Pascal's Triangle to return.

    Returns:
        List[List[int]]: The first n rows of Pascal's Triangle.
        An empty list is returned of n <= 0.
    """
    if n <= 0:
        return []

    # Initialize first row of Pascal's Triangle.
    triangle = [[1]]

    # Generate the remaining rows of Pascal's Triangle.
    while len(triangle) < n:
        prev_row = triangle[-1]
        new_row = [1]   # Start with 1

        for i in range(len(prev_row) - 1):
            # Calculate the sum of adjacent elements
            new_row.append(prev_row[i] + prev_row[i+1])

        new_row.append(1)   # End with 1
        triangle.append(new_row)

    return triangle
