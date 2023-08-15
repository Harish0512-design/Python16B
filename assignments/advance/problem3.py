# 3)Write a Python program to sum all the items in a list using reduce.
from functools import reduce


def sum_of_items(lst):
    return reduce(lambda x, y: x + y, lst)


print(sum_of_items([1, 2, 3, 4]))
