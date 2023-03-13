#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        print()
    else:
        for row in matrix:
            for column in row:
                if column == row[-1]:
                    print("{:d} ".format(matrix[row][column]), end='')
                else:
                    print("{:d}".format(matrix[row][column]), end='')
            print()
