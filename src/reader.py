# coding: utf-8
from src.exceptions import ParseException
from src.parser import WHITE_SPACE


class Reader(object):
    def __init__(self, json_text):
        self.p = 0
        self.length = len(json_text)
        self.json_text = json_text

    def move(self, offset=1):
        new_p = self.p + offset
        self.p = new_p

    def peek(self, offset=1):
        end = self.p + offset
        return self.json_text[self.p: end]

    def read(self, offset=1):
        res = self.peek(offset)
        self.move(offset)
        return res

    def skip_white_space(self):
        while self.peek() in WHITE_SPACE:
            self.move()
