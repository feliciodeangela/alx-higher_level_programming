#!/usr/bin/python3
"""Unittest for max_integer([..])"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Class definition for testing max_integer function"""

    def test_mx(self):
        self.assertEqual(max_integer([5,2,9,0]), 9)

    def test_vals(self):
        self.assertNotIsInstance(max_integer([3,6]), list)
        self.assertNotIsInstance(max_integer("[3,6]"), list)

    def test_expt(self):
        self.assertRaises(TypeError, max_integer, ["23",5,31,8])
        self.assertRaises(TypeError, max_integer, 23)
