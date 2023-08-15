# By using list comprehension, please write a program to print the list
# after removing the 0th, 2nd, 4th,6th numbers in
# [12,24,35,70,88,120,155].
# Hints:
# Use list comprehension to delete a bunch of element from a list.
# Use enumerate() to get (index, value) tuple.

input_lst = [12, 24, 35, 70, 88, 120, 155]
# # adding values which are not at 0, 2, 4, 6 indexes
# output_lst = [val for idx, val in enumerate(input_lst) if idx not in (0, 2, 4, 6)]
output_lst = [val for idx, val in enumerate(input_lst) if idx % 2 != 0]
print(output_lst)
