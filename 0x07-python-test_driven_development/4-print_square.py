#!/usr/bin/python3
"""
4-print_square.py

A module that contains a function to print
a square.
"""


def print_square(size):
    """Prints a square.

    Args:
        size (int): size of the square sides

    Raises:
        TypeError: If `size` is not an integer
        TypeError: If `size` is a negative float
        ValueError: If `size` is negative integer
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")
    
    for symbol in range(size):
        print("#" * size)
