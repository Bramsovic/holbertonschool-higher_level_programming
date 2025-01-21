#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = (tuple_a[0] if len(tuple_a) > 0 else 0,
               tuple_a[1] if len(tuple_a) > 1 else 0)
    tuple_b = (tuple_b[0] if len(tuple_b) > 0 else 0,
               tuple_b[1] if len(tuple_b) > 1 else 0)
    result = ()
    for index in range(len(tuple_b)):
        result += (tuple_a[index] + tuple_b[index],)
    return result
