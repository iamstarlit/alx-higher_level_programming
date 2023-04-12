#!/usr/bin/Python3
"""
A module that returns the list of available attributes
and methods of an object.
"""


def lookup(obj):
    """Returns the list of attributes and methods of an object.

    Args:
       obj (obj: 'str'): name of the object

    Returns:
       list: list of available methods and attributes of ``obj``
    """

    return list(dir(obj))
