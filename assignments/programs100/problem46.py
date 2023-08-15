# Write a program which can map() and filter() to make a list whose
# elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
# Hints:
# Use map() to generate a list.
# Use filter() to filter elements of a list.
# Use lambda to define anonymous functions.

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares_lst = list(map(lambda y: y ** 2, filter(lambda x: x % 2 == 0, input_list)))
print(even_squares_lst)
