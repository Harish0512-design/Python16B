# By using list comprehension, please write a program to print the list
# after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].
# Hints:
# Use list comprehension to delete a bunch of element from a list.
# Use enumerate() to get (index, value) tuple.

input_lst = [12, 24, 35, 70, 88, 120, 155]
output_lst = [v for idx, v in enumerate(input_lst) if idx not in (0, 4, 5)]
print(output_lst)
