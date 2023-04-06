#!/usr/bin/python3
"""My rectangle module"""


class Rectangle(object):
    """Defines a rectangle class"""
    def __init__(self, width=0, height=0):
        """Initializes a rectangle object.

        Args:
            width: rectangle width parameter
            height: rectangle height parameter

        Raises:
            TypeError: If width or height is not an integer
            ValueError: If height or width is < 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrives the width of a rectangle"""
        return self.__widht

    @width.setter
    def width(self, value):
        """Sets the width of a rectangle"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Retrives the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height of a rectangle"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
