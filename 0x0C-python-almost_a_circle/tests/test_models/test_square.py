#!/usr/bin/python3
"""
test_square.py

Unit tests for the Square class.
"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_init(self):
        s1 = Square(5)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

        s2 = Square(10, 2, 3, 4)
        self.assertEqual(s2.id, 4)
        self.assertEqual(s2.size, 10)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 3)

    def test_size(self):
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

        s1.size = 10
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)

    def test_update(self):
        s1 = Square(5)
        s1.update(10)
        self.assertEqual(s1.id, 10)

        s1.update(10, 20)
        self.assertEqual(s1.size, 20)

        s1.update(10, 20, 30)
        self.assertEqual(s1.x, 30)

        s1.update(10, 20, 30, 40)
        self.assertEqual(s1.y, 40)

        s1.update(y=50, x=40, id=20, size=30)
        self.assertEqual(s1.id, 20)
        self.assertEqual(s1.size, 30)
        self.assertEqual(s1.x, 40)
        self.assertEqual(s1.y, 50)

    def test_to_dictionary(self):
        s1 = Square(10, 2, 1)
        s1_dict = s1.to_dictionary()
        expected = {'id': 1, 'size': 10, 'x': 2, 'y': 1}
        self.assertEqual(s1_dict, expected)

    def test_errors(self):
        with self.assertRaises(TypeError):
            s = Square()
        with self.assertRaises(TypeError):
            s = Square(1, 2, 3, 4, 5)
        with self.assertRaises(ValueError):
            s = Square(-1)
        with self.assertRaises(ValueError):
            s = Square(0)
        with self.assertRaises(ValueError):
            s = Square(1, -1, 0)
        with self.assertRaises(ValueError):
            s = Square(1, 0, -1)
        with self.assertRaises(ValueError):
            s = Square(1, -1, -1)
        with self.assertRaises(ValueError):
            s = Square(1, 1, 1, -1)
