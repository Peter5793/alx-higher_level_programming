#!/usr/bin/python3
def roman_to_int(roman_string):
    d = {'I':1, 'V':5, 'X': 10, 'L': 50, 'C':100, 'D':500, 'M':1000}
    prev = 0
    curr = 0
    total = 0
    for i in range(len(roman_string)):
        curr = d[roman_string[i]]
        if curr > prev:
            total = total + curr -2(prev)
        else:
            total += curr
            prev = curr
    return total
