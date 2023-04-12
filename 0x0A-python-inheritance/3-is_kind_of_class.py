#!/usr/bin/python3
"""
A module to check if an object is exactly
an instance of the specified class.
"""


def is_kind_of_class(obj, a_class):
    """Check if ``obj`` is an instance
    of ``a_class``.

    Args:
        obj (obj: 'str'): object name
        a_class (cls: 'str'): class name

    Returns:
        bool: return ``True`` if ``obj`` is an instance
        of ``a_class``, ``Fale`` otherwise
    """

    return isinstance(obj, a_class)
