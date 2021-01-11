#!/usr/bin/python3
"""
Define a class rectangle defined by 1-rectangle.py
"""


class Rectangle:
    """
    define attributes instances
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        intialzie height and width
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >=0')
        self.__width = value

    @property
    def height(self):
        """set the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('width must be >=0')
        self.__height = value

    def area(self):
        """intialize the area of the rectangle"""
        rec_area = self.__height * self.__width
        return rec_area

    def perimeter(self):
        """Intitialize the perimeter method"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2*self.height + 2*self.width)

    def __str__(self):
        """prints graphical represnation of rectangle"""
        rect = ""
        if self.__height == 0 or self.__width == 0:
            return rect
        for i in range(self.__height):
            rect += '#' * self.__width
            if i != self.__height - 1:
                rect += '\n'
        return rect

    def __repr__(self):
        """returns traditional formal string"""
        repr_str = self.__class__.__name__
        return "{}({},{})".format(repr_str, self.__width, self.__height)

    def __del__(self):
        """
        Destroy rectangle
        """
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
