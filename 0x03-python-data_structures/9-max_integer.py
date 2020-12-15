#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_1 = 0
    for i in my_list:
        if i > max_1:
            max_1 = i
    return (max_1)
