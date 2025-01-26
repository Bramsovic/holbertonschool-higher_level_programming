#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for i, column in enumerate(line):
            if i == len(line) - 1:
                print("{:d}".format(column), end="")
            else:
                print("{:d}".format(column), end=" ")
        print()
