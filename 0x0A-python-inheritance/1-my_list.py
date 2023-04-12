#!/usr/bin/python3
"""
A module to print sorted list.

This module inherits from the list class.
"""


class MyList(list):
    """Defines a MyList Class."""

    def print_sorted(self):
        """Prints a sorted list."""
        print(sorted(self))
