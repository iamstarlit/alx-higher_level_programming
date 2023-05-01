#!/usr/bin/python3
"""
test_base.py

Test file for the `base.py` module in the models package.
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Class to perform unit tests on Base class."""

    def test_id(self):
        b1 = Base()
        self.assertEqual(print(b1.id), 1)
