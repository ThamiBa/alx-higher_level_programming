#!/usr/bin/python3


def multiply_list_map(my_list=[], number=0):
    """
    A fct that returns a list with all val multi by a nb without using any lps
    """
    return (list(map((lambda i: i * number), my_list)))
