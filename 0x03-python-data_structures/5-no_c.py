#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return None
    dict = {ord('c'): None, ord('C'): None}
    my_string_2 = my_string.translate(dict)
    return my_string_2
