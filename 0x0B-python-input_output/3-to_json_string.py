#!/usr/bin/python3
"""
3-to_json_string.py
"""

import json


def to_json_string(my_obj):
    """Returns JSON representantion of a string object.

    Args:
        my_obj (obj: str): string object parameter

    Returns:
        str: JSON representation of a string object.
    """
    return json.dumps(my_obj)
