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
    with open(filename, mode='r', encoding="utf-8") as f:
        lines = f.readlines()

        # Create an empty list to store modified lines
        new_lines = []

        # Iterate over the lines and modify them
        for line in lines:
            # Append the original lines to the new_list
            new_lines.append(line)

            if search_string in line:
                new_lines.append(new_string)

    # open file in write mode and write the modified lines
    with open(filename, mode='w', encoding="utf-8") as f:
        f.writelines(new_lines)
