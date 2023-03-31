#!/usr/bin/python3

# 0-square.py by Paul John
"""A module that defines a square"""


class Square(object):
    """A class that represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes this Square Class
        Args:
            size - size of the square defined
            position: square coordinates
        """

        self.size = size
        self.position = position

    def __str__(self):
        self.my_print()

    @property
    def size(self):
        """Retrives size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        """ Sets the value of size of the square safely
        Raises:
            TypeError: if size is not int
            ValueError: if size is negative number
            """

        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    @property
    def position(self):
        """Property of square coordinates"""

        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square
        Args:
            value - tuple of two positive coordinates
        Raises:
            TypeError: if value is not a tuple or positive integer
        """

        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = value

    def area(self):
        """
        Calculates the area of the square
        Returns: The square of size
        """

        return (self.__size ** 2)

    def pos_print(self):
        """returns the position of square in spaces"""

        pos = ""
        if self.size == 0:
            return "\n"
        for w in range(self.position[1]):
            pos += "\n"
        for w in range(self.size):
            for i in range(self.position[0]):
                pos += " "
            for j in range(self.size):
                pos += "#"
            pos += "\n"
        return pos

    def my_print(self):
        """print the square in position """

        print(self.pos_print(), end='')
