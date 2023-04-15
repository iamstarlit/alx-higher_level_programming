#!/usr/bin/python3
"""
8-class_to_json.py

Returns the dictionary description with simple data structure
(list, dictionary, string, integer, and boolean for
JSON searialization of an object.
"""


def class_to_json(obj):
    """Return the dictionary description with simple data structure.

    Args:
       obj (obj: 'str'): an object parameter

    Returns:
        dict: simple dictinary description.
    """
    # use object __dict__
    return obj.__dict__
