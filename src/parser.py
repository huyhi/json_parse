# coding: utf-8
from src.exceptions import ParseException

INVOLUTION_SIGN = {'e', 'E'}
POSITIVE_NEGATIVE_SIGN = {'-', '+'}
WHITE_SPACE = {' ', '\t', '\r', '\n'}
_0TO9 = {str(i) for i in range(10)}
_1TO9 = {str(i) for i in range(1, 10)}
TRANSFERRED_CHAR = {
    '\"': '\"',
    '\\': '\\',
    '/': '/',
    'b': '\b',
    'f': '\f',
    'n': '\n',
    'r': '\r',
    't': '\t'
}


def parse(r):
    func_map = {
        '{': parse_object,
        '[': parse_array,
        '"': parse_string,
        'n': parse_null,
        't': parse_true,
        'f': parse_false
    }

    r.skip_white_space()
    character = r.peek()

    if character in _0TO9 | POSITIVE_NEGATIVE_SIGN:
        func = parse_number
    elif character in func_map:
        func = func_map.get(character)
    else:
        raise ParseException()
    return func(r)


def parse_true(r):
    if r.read(4) == 'true':
        return True
    raise ParseException()


def parse_false(r):
    if r.read(5) == 'false':
        return False
    raise ParseException()


def parse_null(r):
    if r.read(4) == 'null':
        return None
    raise ParseException()


# http://www.ecma-international.org/publications/files/ECMA-ST/ECMA-404.pdf
def parse_number(r):
    # 记录开始解析时的指针位置
    start = r.p
    is_decimal = False

    if r.peek() == '-':
        r.move()

    if r.peek() == '0':
        r.move()
    else:
        if r.read() not in _1TO9:
            raise ParseException()
        while r.peek() in _0TO9:
            r.move()

    if r.peek() == '.':
        r.move()
        is_decimal = True
        if r.read() not in _0TO9:
            raise ParseException()
        while r.peek() in _0TO9:
            r.move()

    if r.peek() in INVOLUTION_SIGN:
        r.move()
        is_decimal = True
        if r.peek() in POSITIVE_NEGATIVE_SIGN:
            r.move()
        if r.peek() not in _0TO9:
            raise ParseException()
        while r.peek() in _0TO9:
            r.move()

    end = r.p
    slice = r.json_text[start: end]
    return float(slice) if is_decimal else int(slice)


def parse_string_generator(r):
    if r.read() != '\"':
        raise ParseException()

    while r.peek() != '\"':
        if r.peek() == '\\':
            r.move()
            # 解析正常的转义字符
            if r.peek() in TRANSFERRED_CHAR:
                yield TRANSFERRED_CHAR.get(r.read())
            else:
                raise ParseException()
        else:
            if ord(r.peek()) < 0x20:
                raise ParseException()
            else:
                yield r.read()
    # 最后再移动一下，解析完成后 p 应该是指向后一个引号的
    r.move()


def parse_string(r):
    return ''.join(parse_string_generator(r))


def parse_array_generator(r):
    res = []
    if r.read() != '[':
        raise Exception()

    while r.peek() != ']':
        # res.append(parse(r))
        yield parse(r)
        r.skip_white_space()
        if r.peek() == ',':
            r.move()
            if r.peek() == ']':
                raise ParseException()
    r.move()

    return res


def parse_array(r):
    return list(parse_array_generator(r))


def parse_object(r):
    res = {}
    if r.read() != '{':
        raise ParseException()

    while r.peek() != '}':
        r.skip_white_space()
        key = parse_string(r)
        r.skip_white_space()
        if r.read() != ':':
            raise ParseException()
        r.skip_white_space()
        value = parse(r)
        r.skip_white_space()
        if r.peek() == ',':
            r.move()
            if r.peek() == '}':
                raise ParseException()
        res[key] = value
    r.move()

    return res
