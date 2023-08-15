# By using list comprehension, please write a program to print the list
# after removing the value 24 in [12,24,35,24,88,120,155].
# Hints:
# Use list's remove method to delete a value.

input_lst = [12, 24, 35, 24, 88, 120, 155]
# deletes only first occurances
# input_lst.remove(24)
output_lst = [val for val in input_lst if val != 24]
print(output_lst)
