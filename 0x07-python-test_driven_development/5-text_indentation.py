#!/usr/bin/python3
"""
5-text_indentation.py

A module that contains a function that prints
two newlines after each specified symbol.
"""

def text_indentation(text):
    """Prints two new lines after a specified character.

    The specified characters are `.`, `?`, and `:` in a list
    called `separators`. The function removes extra spaces at
    the beginning and end of the text.

    Args:
        text (str): text parameter to check 

    Raises:
        TypeError: If `text` is not a string
    """

    # Check if the input text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # List of symbols that will be used as separators
    separators = [".", "?", ":"]

    # Removing extra spaces at the beginning of the text
    index = 0
    while index < len(text) and text[index] == " ":
        index += 1

    # Printing the text with two new lines after each symbol
    # in the `separators` list.
    while index < len(text):
        print(text[index], end="")

        # Add two new lines after each separator.
        if text[index] == "\n" or text[index] in separators:
            if text[index] in separators:
                print("\n")
            index += 1

            # Remove extra spaces after each separator.
            while index < len(text) and text[index] == " ":
                index += 1
            continue
        index += 1
