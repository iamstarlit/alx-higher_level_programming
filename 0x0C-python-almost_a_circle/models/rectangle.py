#!/usr/bin/python3
"""
rectangle.py

A module that contains a Rectangle class that inherits from Base class.
"""

# Import Base Class
from models.base import Base


class Rectangle(Base):
    """A Rectangle class; sub-class of Base Class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the instance of sub-class Reactangle.

        Args:
            width (int): `width` parameter.
            height (int): `height` parameter.
            x (int): `x` horizontal coordinate parameter.
            y (int):` y` vertical coordinate parameter.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of Rectangle.

        Returns:
            int: The width of rectangle.
        """
        return self.__width

    @width.setter
    def width(self, width):
        """Set the width of Rectangle.

        Args:
           width (int): width of Rectangle.
        """
        self.__width = width

    @property
    def height(self):
        """Get the height of Rectangle.
        Returns:
            int: height of Rectangle
        """
        return self.__height

    @height.setter
    def height(self, height):
        """Set the height of Rectangle.

        Args:
            height (int): height of Rectangle.
        """
        self.__height = height

    @property
    def x(self):
        """Get horizontal coordinate `x` of the Reactangle.

        Returns:
            int: horizontal coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, x):
        """Set horizontal coordinate `x` of the Rectangle.

        Args:
            x (int): horizontal coordinate of the Rectangle.
        """
        self.__x = x

    @property
    def y(self):
        """Get vertical coordinate `y` of the Rectangle.

        Returns:
            int: vertical coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, y):
        """Set vertical coordinata `y` of the Rectangle.

        Args:
            y (int): vertical coodrinate of the Rectangle.
        """
        self.__y = y
