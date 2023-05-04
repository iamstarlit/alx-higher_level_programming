#!/usr/bin/python3
"""
test_base.py

Test file for the `base.py` module in the models package.
"""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_no_id(self):
        """
        Test that a Base instance is created with an id of 1 when no id is passed.
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_positive_id(self):
        """
        Test that a Base instance is created with the correct id when a positive integer is passed.
        """
        b2 = Base(2)
        self.assertEqual(b2.id, 2)

    def test_negative_id(self):
        """
        Test that a ValueError is raised when a negative integer is passed as an id.
        """
        with self.assertRaises(ValueError):
            b3 = Base(-3)

    def test_float_id(self):
        """
        Test that a TypeError is raised when a float is passed as an id.
        """
        with self.assertRaises(TypeError):
            b4 = Base(1.2)

    def test_string_id(self):
        """
        Test that a TypeError is raised when a string is passed as an id.
        """
        with self.assertRaises(TypeError):
            b5 = Base("hello")

if __name__ == '__main__':
    unittest.main()
