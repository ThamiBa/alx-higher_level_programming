#!/usr/bin/python3


def square_matrix_map(matrix=[]):
    """
    The function that computes the square value of all intgs of a matrix using
    """
    return (list(map(lambda x: list(map(lambda y: y**2, x)), matrix)))
