# Please write a program to print the list after removing delete even
# numbers in [5,6,77,45,22,12,24].
# Hints:
# Use list comprehension to delete a bunch of element from a list.

input_lst = [5, 6, 77, 45, 22, 12, 24]
output_lst = [x for x in input_lst if x % 2 != 0]
print(output_lst)
