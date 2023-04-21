#!/usr/bin/python3
"""
3-say_my_name.py

This module has a function that prints a name
provided.
"""


def say_my_name(first_name, last_name=""):
    """A function that prints a name.

    Args:
        first_name (str): First name parameter
        last_name (str): Last name parameter

    Raises:
        TypeError: If `first_name` or `last_name` is not a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
