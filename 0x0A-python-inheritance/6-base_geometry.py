#!/usr/bin/python3
"""A module that contains a BaseGeometry Class."""


class BaseGeometry(object):
    """Defines a BaseGeometry class."""

    def area(self):
        raise Exception("area() is not implemented")
