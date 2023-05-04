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
        # Check if width is an integer.
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        # Check if width is negative or zero
        if width <= 0:
            raise ValueError("width must be > 0")

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
        # Check if height is an integer.
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        # Check if height is negative or zero
        if height <= 0:
            raise ValueError("height must be > 0")

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
        # Check if `x` is not an integer
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        # Check if `x` is negative or zero
        if x < 0:
            raise ValueError("x must be > 0")

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
        # Check if `y` is not an integer
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        # Check if `y` is negative or zero
        if y < 0:
            raise ValueError("y must be > 0")

        self.__y = y
