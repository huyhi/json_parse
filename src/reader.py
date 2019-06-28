# coding: utf-8
from src.exceptions import ParseException
from src.parser import WHITE_SPACE


class Reader(object):
    def __init__(self, json_text):
        self.p = 0
        self.line_number = 1
        self.char_index = 1
        self.json_text = json_text

    def move(self, offset=1):
        if self.peek() == '\n':
            self.line_number += 1
            self.char_index = 1
        else:
            self.char_index += 1
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

    def expect(self, character):
        if self.read(len(character)) != character:
            self.raise_exception("expect '{}'".format(character))

    def raise_exception(self, error_message):
        raise ParseException(error_message, self.line_number, self.char_index)
