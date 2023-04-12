#!/usr/bin/python3
"""A module to that contains MyInt sub class."""


class MyInt(int):
    """Defines MyInt sub class."""

    def __eq__(self, other):
        """returns != check."""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """returns == check"""
        return int.__eq__(self, other)
