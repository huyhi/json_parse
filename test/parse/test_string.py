# coding: utf-8
import unittest

from test.parse.base import parse_fun


class TestNumber(unittest.TestCase):
    def test_main(self):
        self.assertEqual('', parse_fun('""'))
        self.assertEqual('a', parse_fun('"a"'))
        self.assertEqual('ab', parse_fun('"ab"'))

        self.assertEqual('\\', parse_fun('"\\\\"'))
        self.assertEqual('a\n', parse_fun('"a\\n"'))
        self.assertEqual('a\nb', parse_fun('"a\\nb"'))
        self.assertEqual('a\n\b123', parse_fun('"a\\n\\b123"'))
        self.assertEqual('a/123', parse_fun('"a\\/123"'))

        self.assertEqual(True, parse_fun('true'))
        self.assertEqual(False, parse_fun('false'))
        self.assertEqual(None, parse_fun('null'))
