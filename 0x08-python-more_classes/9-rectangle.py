#!/usr/bin/python3
"""A module to represent a rectangle"""


class Rectangle(object):
    """Defines a rectangle class.

    Attributes:
        number_of_instances (int): number of instances (objects)
        print_symbol: string representantion symbol
    """

    number_of_instances = 0
    print_symbol = "#"

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

        # Increment 'number_of_instances'
        Rectangle.number_of_instances += 1

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangle = ""

        for symbol in range(self.__height):
            rectangle += (str(Rectangle.print_symbol) * self.__width) + "\n"
        return rectangle[:-1]

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")

        # Decrement 'number_of_instances'
        Rectangle.number_of_instances -= 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """A static method that checks for the bigger rectangle.

        Args:
            rect_1 (:obj: 'str'): The first reactangle object
            rect_2 (:obj: 'str'): The second reactangle object

        Raises:
            TypeError: If 'rect_1' or 'rect_2' is not an instance
                of Rectangle class

        Returns:
            'rect_1' If 'rect_1' is >= to 'rect_2', 'rect_2' otherwise
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """class method that returns a square of 'size'.

        Args:
            size (int): size of sides of a square

        Returns: new Rectangle instance
        """

        return cls(size, size)
