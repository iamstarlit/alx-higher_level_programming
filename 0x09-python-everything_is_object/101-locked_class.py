#!/usr/bin/python3
"""
A module that contains a class that
avoids dynamically creating attributes
"""


class LockedClass(object):
    """Defines a LockedClass class"""

    __slots__ = ['first_name']
