#!/usr/bin/python3
"""
A module that contains a class that
avoids dynamically creating attributes
"""


class LockedClass(object):
    __slots__ = ['first_name']

    def __init__(self):
        """Initializes an instance of LockedClass class."""
        pass
