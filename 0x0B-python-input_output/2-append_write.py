#!/usr/bin/python3
"""
2-append_write.py
"""


def append_write(filename="", text=""):
    """Appends a string to a file.

    Args:
        filename (str): file name parameter.
        text (str): text to append to a file.

    Returns:
       int: number of characters written to a file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
