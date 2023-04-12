#!/usr/bin/python3
"""A module that contains a BaseGeometry Class."""


class BaseGeometry(object):
    """Defines a BaseGeometry class."""

    def area(self):
        """Defines area of a geometry."""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method that validates ``value``.

        Args:
           name (str): name of value parameter
           value (int): value parameter

        Raises:
            TypeError: if ``value`` is not an integer
            ValueError: if ``value`` is not > 0

        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
