#!/usr/bin/python3
"""
0-add_integer.py

This module defines a function ``add_integer()`` that
adds two integers.
"""


def add_integer(a, b=98):
    """Adds two integers.

    Args:
        a (int): first number parameter
        b (int): second number parameter

    Raises:
       TypeError: if `a` or `b` is not an integer.

    Returns:
        int: the sum of `a` and `b`
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer.")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer.")

    return int(a + b)
