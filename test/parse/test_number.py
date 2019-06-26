# coding: utf-8
import unittest

from test.parse.base import parse_fun


class TestNumber(unittest.TestCase):
    def test_main(self):
        self.assertEqual(0.0, parse_fun('0'))
        self.assertEqual(0.0, parse_fun('0.0'))
        self.assertEqual(0.0, parse_fun('-0'))
        self.assertEqual(0.0, parse_fun('-0.0'))

        self.assertEqual(1.0, parse_fun('1'))
        self.assertEqual(-1.0, parse_fun('-1'))
        self.assertEqual(-1.0, parse_fun('-1.0'))

        self.assertEqual(50.0, parse_fun('5e1'))
        self.assertEqual(50.0, parse_fun('5E+1'))
        self.assertEqual(50.0, parse_fun('5E+001'))
        self.assertEqual(50.0, parse_fun('5.0E1'))

        self.assertEqual(3.1415, parse_fun('3.1415'))

