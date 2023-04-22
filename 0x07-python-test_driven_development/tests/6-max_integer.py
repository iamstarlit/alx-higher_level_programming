#!/usr/bin/python3
"""
6-max_integer.py

A module that contains a function that returns the
maximum integer in a list.
"""


def max_integer(list=[]):
    """Function to find and return the max integer.

    It finds the max integer in a list, and returns None
    if the list is empty.
    """

    # Check empty list
    if len(list) == 0:
        return None

    # Initial result
    result = list[0]

    # check the max integer
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1

    return result
