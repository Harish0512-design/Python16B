# 1.
# Write a program which will find all such numbers which are divisible
# by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence
# on a single line.

# def check(min_val, max_val):
#     lst = []
#     for i in range(min_val, max_val + 1):
#         if i % 7 == 0 and i % 5 != 0:
#             # print(i, end=",")
#             lst.append(str(i))
#     return ",".join(lst)
#
#
# r = check(2000, 3200)
# print(r)

# 2
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a
# single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.

# def find_factorial(input_number):
#     fact = 1
#     while input_number > 0:
#         fact *= input_number
#         input_number = input_number - 1
#     return fact
#
#
# if __name__ == "__main__":
#     input_val = int(input("Enter a number"))
#     print(find_factorial(input_val))

# 3
# With a given integral number n, write a program to generate a
# dictionary that contains (i, i*i) such that is an integral number
# between 1 and n (both included). and then the program should print the
# dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.
# Consider use dict()

# # getting input from the user
# user_input = int(input())
# # creating a dict with num as key and its square as value from 1 to user_input using dictionary comprehension
# res_dict = {i: i * i for i in range(1, user_input + 1)}
# print(res_dict)


# 4.
# Write a program which accepts a sequence of comma-separated numbers
# from console and generate a list and a tuple which contains every
# number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')
# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.
# tuple() method can convert list to tuple

# ls = [int(x) for x in input().split(',')]
# print(ls)
# # converting list to tuple
# print(tuple(ls))

# 5.
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
# Hints:
# Use __init__ method to construct some parameters

# class Sample:
#     def __init__(self):
#         self.name = None
#
#     def get_string(self):
#         self.name = input()
#
#     def print_string(self):
#         print(self.name.upper())
#
#     def test(self):
#         self.get_string()
#         self.print_string()
#
#
# res_obj = Sample()
# res_obj.test()

# 6.
# Write a program that calculates and prints the value according to the
# given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a
# comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to
# the program:
# 100,150,180
# The output of the program should be:
# 18,22,24
# Hints:
# If the output received is in decimal form, it should be rounded off to
# its nearest value (for example, if the output received is 26.0, it
# should be printed as 26)
# In case of input data being supplied to the question, it should be
# assumed to be a console input.

# import math
#
# # taking input from user using list comprehension
# input_values = [int(x) for x in input().split(',')]
# output = list(map(lambda d: str(math.floor(math.sqrt(((2 * 50 * d) / 30)))), input_values))
# # joining all list items using ',' and join operator
# print(','.join(output))

# 7