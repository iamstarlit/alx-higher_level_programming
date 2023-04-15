#!/usr/bin/python3
"""
0-read_file.py module.
"""


def read_file(filename=""):
    """Reads a text file UTF8 and print to stdout.

    Args:
        filename: file name

    Raises:
        Exception: if file cannot be opened
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end='')
