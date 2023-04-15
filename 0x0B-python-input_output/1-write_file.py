#!/usr/bin/python3
"""
1-write_file.py
"""


def write_file(filename="", text=""):
    """Writes to a file UTF8 format.

    Args:
       filename: file name parameter
       text: text parameter
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
