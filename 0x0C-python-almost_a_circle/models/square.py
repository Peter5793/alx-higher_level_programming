#!/usr/bin/python3
"""Inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    intialize square definition
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overloading string method"""
        return ("[Sqaure] ({}) {}/{} - {}".format
                (self.id, self.x, self.y, self.height))

    @property
    def size(self):
        """getter for width"""
        return self.width

    @size.setter
    def size(self, size):
        """size setter"""
        self.width = size
        self.height = size
