#!/usr/bin/python3
"""
Function that adds two integers
>>> add_integer(2,4)
6
"""


def add_integer(a, b=98):
    """
    return the sum of two integers
    """
    if a is None:
        raise TypeError('a must be an integer')
    if b is None:
        raise TypeError('b must be an integer')
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')
    else:
        return int(a) + int(b)
