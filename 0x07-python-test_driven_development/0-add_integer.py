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
    arguments = []
    for i, params in [(a, 'a'), (b, 'b')]:
        if isinstance(i, int):
            arguments.append(i)
        elif isinstance(i, float):
            arguments.append(int(i))
        else:
            raise TypeError("{} must be an integer".format(params))

    return sum(arguments)
