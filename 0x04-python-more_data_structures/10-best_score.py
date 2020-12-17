#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None or a_dictionary == {}:
        return None
    max_item = max(zip(a_dictionary.values(), a_dictionary.keys()))
    if max_item == 0:
        return None
    return max_item[1]
