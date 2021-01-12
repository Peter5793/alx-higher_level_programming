#!/usr/bin/python3
"""
Define a locked class
"""


class LockedClass:
    """ Prevents the userfrom dynamically creating a new instance attribute
    """
    __slots__ = ['first_name']
