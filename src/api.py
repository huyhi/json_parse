# coding: utf-8
from src.parser import parse
from src.reader import Reader


def json_decode(json_text):
    return parse(Reader(json_text))


if __name__ == '__main__':
    json_text = '''
    {
        "author": "annhuny",
        "date": "20190625",
        "version": 1.0,
        "type": ["array", "string", "number", "object"],
        "test": [
            {
                "first": "1"
            },
            {
                "second": "2"
            }
        ]
    }
    '''
    print(json_decode(json_text))
