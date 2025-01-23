#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for index in range(len(matrix)):
        for cloumn in range(len(matrix[index])):
            print("{:d}".format(matrix[index][cloumn]), end=" ")
        print()
