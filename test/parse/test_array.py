# coding:utf-8
import unittest

from test.parse.base import parse_fun


class TestArray(unittest.TestCase):
    def test_main(self):
        self.assertEqual([], parse_fun('[]'))
        self.assertEqual([1], parse_fun('[1]'))
        self.assertEqual([1, 2], parse_fun('[1, 2]'))
        self.assertEqual([1, 2], parse_fun('[1,2]'))
        self.assertEqual([1, []], parse_fun('[1,  []]'))
        self.assertEqual([1, [1, 2]], parse_fun('[1,  [1,2]]'))
        self.assertEqual([1, [1, 2, '123']], parse_fun('[1,  [1,2, "123"]]'))
        self.assertEqual([1, [1, 2, True]], parse_fun('[1,  [1,2, true]]'))
        self.assertEqual([1, [1, 2, 1.2]], parse_fun('[1,  [1,2,1.2]]'))
