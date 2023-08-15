# Please write a program which prints all permutations of [1,2,3]
# Hints:
# Use itertools.permutations()

import itertools

res = list(itertools.permutations([1, 2, 3]))
print(res)
