#!/usr/bin/python3
"""
Checks if the object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    if type(obj) is a_class:
        return True
    else:
        return False
