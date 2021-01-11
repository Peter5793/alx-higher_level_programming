#!/usr/bin/python3
"""
Define a class rectangle based on 0-rectangle.py
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """
        Intialize the height and the width
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """set the width of the rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >=0')
        self.__width = value

    @property
    def height(self):
        """set the height of the rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('height must be >=0')
        self.__height = value
