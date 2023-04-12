#!/usr/bin/Python3

def lookup(obj):
    """Returns the list of attributes and methods of an object.

    Args:
       obj (obj: 'str'): name of the object

    Returns:
       list: list of available methods and attributes of ``obj``
    """

    return list(dir(obj))
