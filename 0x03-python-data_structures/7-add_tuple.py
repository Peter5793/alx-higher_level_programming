#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    if len_a == 0 and len_b == 0:
        s_tuple = (0, 0)
    elif len_a == 1 and len_b == 1:
        s_tuple = (tuple_a[0] + tuple_b[0], 0)
    elif len_a == 1 and len_b != 0:
        s_tuple = (tuple_a[0] + tuple_b[0], tuple_b[1])
    elif len_b == 1 and len_a != 0:
        s_tuple = (tuple_b[0] + tuple_a[0], tuple_a[1])
    elif len_b == 0 and len_a != 0:
        s_tuple = (tuple_a[0], tuple_a[1])
    elif len_a == 0 and len_b != 0:
        s_tuple = (tuple_b[0], tuple_b[1])
    else:
        s_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return (s_tuple)
