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
        self.__width = value
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >=0')
        
    @property
    def height(self):
        """set the height of the rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        self.__height = value
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >=0')
