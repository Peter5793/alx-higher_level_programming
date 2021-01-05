#!/usr/bin/python3
"""class square that defines a square by 1-square.py"""


class Square:
    """class Square with private instance atribute size"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        """initialization of new square with size argument"""
        self._size = size
