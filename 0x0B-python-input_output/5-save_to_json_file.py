#!/usr/bin/python3
"""
5-save_to_json_file.py

Writes an object to a text file
using JSON representantion.
"""

import json


def save_to_json_file(my_obj, filename):
    """Writes to an object to a text file using JSON representation.

    Args:
        my_obj (obj: 'str'): string object
        filenam (str): file name argument
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json_text = json.dumps(my_obj)
        f.write(json_text)
