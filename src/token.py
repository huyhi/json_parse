# coding:utf-8
from enum import Enum, unique


@unique
class TokenType(Enum):
    TRUE = 0
    NUMBER = 3


class Token(object):
    def __init__(self, type):
        self.type = type
