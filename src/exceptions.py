# coding: utf-8


class BaseParseException(Exception):
    def __str__(self):
        return self.message


class ParseException(BaseParseException):
    def __init__(self, error_message, line_number, char_index):
        self.message = "{} at {}:{}".format(error_message, line_number, char_index)
