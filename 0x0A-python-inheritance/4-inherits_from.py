#!/usr/bin/python3
"""
A module to check if an object inherits from
a class.
"""


def inherits_from(obj, a_class):
    """checks if ``obj`` inherits from ``a_class``.

    Args:
        obj (obj: 'str'): object name parameter
        a_class (cls: 'str'): class name parameter

    Returns:
       bool: returns ``True`` if ``obj`` inherits from
       ``a_class``, and ``False`` otherwise.
    """

    if type(obj) is a_class:
        return False

    return isinstance(obj, a_class)
