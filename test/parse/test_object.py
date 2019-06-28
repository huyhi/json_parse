# coding:utf-8
import unittest

from test.parse.base import parse_fun


class TestObject(unittest.TestCase):
    def test_main(self):
        self.assertEqual({}, parse_fun('{}'))
        self.assertEqual({'1': 'a'}, parse_fun('{"1": "a"}'))
        self.assertEqual({'key': ['a', 'b']}, parse_fun('{"key": ["a", "b"]}'))
        self.assertEqual({'key': True}, parse_fun('{"key": true}'))
        self.assertEqual({'key': {'nums': [1.1, 2, 3]}}, parse_fun('{"key": {"nums": [1.1, 2, 3]}}'))
