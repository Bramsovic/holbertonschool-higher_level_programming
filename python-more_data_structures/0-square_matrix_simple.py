#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = []
    for list in matrix:
        sub_list = []
        for value in list:
            sub_list.append(value ** 2)
        new_list.append(sub_list)
    return new_list
