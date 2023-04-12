#!/usr/bin/python3
"""
A module to check if an object is an instance
of a specified class.
"""


def is_same_class(obj, a_class):
    """checks if ``obj`` is an instance of ``a_class``.

    Args:
        obj (obj: 'str'): an object
        a_class (cls: 'str'): a class

    Returns:
        bool: ``True`` if ``obj`` is an instance of
        ``a_class`` otherwise ``False``.
    """

    return type(obj) is a_class
