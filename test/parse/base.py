# coding: utf-8

from src.parser import parse
from src.reader import Reader


def parse_fun(json_text):
    return parse(Reader(json_text))
