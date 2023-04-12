#!/usr/bin/python3
"""
A module that adds an attribute to a class.
"""


def add_attribute(obj, name, value):
    """adds a new attribute to an object.

    Args:
        obj (obj: 'str'): object name parameter
        name (str): attribute name parameter
        value: attribute value parameter

    Raises:
        TypeError: if attribute can't be added

    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
