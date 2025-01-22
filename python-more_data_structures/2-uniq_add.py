#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return 0
    elif len(my_list) == 1:
        return my_list[0]
    my_list = set(my_list)
    result = sum(my_list)
    return result
