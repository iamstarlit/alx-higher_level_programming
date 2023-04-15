#!/usr/bin/python3
"""
6-load_from_json_file.py

Creates an object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """Loads an object from a JSON file.

    Args:
        filename (str): file name parameter.
    """
    with open(filename, mode="r") as f:
        return json.load(f)
