#!/usr/bin/python3
"""
class that inherits from list
"""


class myList(list):
    """
    myList is a class with public method print_sorted
    """
    def print_sorted(self):
        print(sorted(self))
