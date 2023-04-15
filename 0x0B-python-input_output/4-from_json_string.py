#!/usr/bin/python3
"""
4-from_json_string.py

Returns an object(Python data structure) represented
by a JSON string.
"""

import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string.

    Args:
       my_str (JSON: 'str'): JSON string

    Returns:
       obj: Python data structure object
    """
    return json.dumps(my_str)
