#!/usr/bin/python3
"""A module that contains a Rectangle Sub Class."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a Sub Class of BaseGeometry, Rectangle."""

    def __init__(self, width, height):
        """Initializes an instance of Rectangle sub class.

        Args:
            width (int): width of a rectangle
            height (int): height of a rectangle

        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Defines string representantion of a class."""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

    def area(self):
        """Defines an area method."""
        return self.__width * self.__height
