#!/usr/bin/python3
"""Unittest for max_integer([..])"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Class definition for testing max_integer function"""

    def test_mx(self):
        self.assertEqual(max_integer([5,2,9,0]), 9)
        self.assertEqual(max_integer([2]), 2)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([100, 33, 12, 34]), 100)
        self.assertEqual(max_integer([-1, 3, -7, 8]), 8)

    def test_vals(self):
        self.assertNotIsInstance(max_integer([3,6]), list)
        self.assertNotIsInstance(max_integer("[3,6]"), list)

    def test_expt(self):
        self.assertRaises(TypeError, max_integer, ["23",5,31,8])
        self.assertRaises(TypeError, max_integer, 23)
