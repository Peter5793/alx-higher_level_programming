#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        print()
    else:
        for row in range(len(matrix)):
            for column in range(len(matrix)):
                if row != len(matrix[row])-1:
                    print("{:d} ".format(matrix[row][column]), end='')
                else:
                    print("{:d}".format(matrix[row][column]), end='')
            print()
