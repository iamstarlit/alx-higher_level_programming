#!/usr/bin/python3
"""
100-append_after.py

Defines a function that inserts a line of text to a file,
after each line containing specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """Appends to a text file after a line containing specified text.

    Args:
        filename (str): file name parameter
        search_string (str): string to insert text after.
        new_string (str): text to insert into a file.
    """
    text = ""

    with open(filename, mode="w+", encoding="utf-8") as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string

        f.write(text)
