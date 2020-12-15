#!/usr/bin/python3
def multiple_returns(sentence):
    len_sen = len(sentence)
    if len_sen == 0:
        char = "None"
    else:
        char = sentence[0]
    return len_sen, char
