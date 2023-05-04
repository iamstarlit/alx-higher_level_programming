#!/usr/bin/python3
"""
test_base.py

Test file for the `base.py` module in the models package.
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Class to perform unit tests on Base class."""

    def test_default_id(self):
        """Test instantiation with default id."""
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_given_id(self):
        """Test instantiation with given id."""
        b2 = Base(12)
        self.assertEqual(b2.id, 12)

    def test_negative_id(self):
        """Test with negative id."""
        with self.assertRaises(ValueError):
            b3 = Base(-3)

    def test_invalid_id(self):
        """Test with invalid id: float and string."""
        with self.assertRaises(TypeError):
            b4 = Base(4.5)
            b5 = Base("Five")
