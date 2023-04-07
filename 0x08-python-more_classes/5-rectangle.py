#!/usr/bin/python3
"""A module to represent a rectangle"""


class Rectangle(object):
    """Defines a rectangle class"""

    def __init__(self, width=0, height=0):
        """Initializes a rectangle object.

        Args:
            width: rectangle width parameter
            height: rectangle height parameter

        Raises:
            TypeError: If 'width' or 'height' is not an integer
            ValueError: If 'height' or 'width' is < 0
        """
        self.width = width
        self.height = height

    def __str__(self) -> str:
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = ""
        for column in range(self.__height):
            for row in range(self.__width):
                rectangle += "#"
            if column < self.__height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")

    @property
    def width(self):
        """Retrives the width of a rectangle"""
        return self.__width

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

    def area(self):
        """Returns area of a rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """Returns perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__height + self.__width))
