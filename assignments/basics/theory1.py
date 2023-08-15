# What is the difference between a parameter and an argument?

# The values which are defined at the time of developing the function are called parameters
# def add(a,b): # parameters,
#     return a+b

# the values which are passed at the time of function call are called arguments.
# add(3,4) # arguments

# 1. positional arguments  add(3,4)
# 2. default arguments add(3,b=4)
# 3. variable length arguments add(*args)(defined during function call) # stores values as a tuple
# 4. keyword arguments add(a=3,b=4) add(**kwargs) # stores values as a dict


# All functions in Python by default return …?
# def funnc() -> None:, def funcc():-> None
# returns None

# What are keyword arguments and when should we use them?
# Keyword arguments are the values which we pass during the function call by as key value pair
# where key represents the parameter
# when we have to assign a value to specific parameter without following position of parameters

# How can we make a parameter of a function optional?
# by assigning None as default for the parameter while function design
# def add(a,b,c=None):

# What happens when we prefix a parameter with an asterisk (*)?
# the parameter with * prefix can take multiple values as input and stores it in a tuple
# this must given as a last parameter
# def add(a,b,*c):
#     for i in c:
#         print(a+b+c)


# What about two asterisks (**)?
# the paramter with prefix ** can take arguments as key-value pairs and store them as dictionary
# def add(**kwargs):
#     for k, v in kwargs.items():
#         print(k, ",", v)
#     print(kwargs)
#
#
# add(a=1, b=2, c=4, d=5)


import sys

# a = ""
# x = ""
# n = sys.getsizeof(x) # 49 bytes
# print(n)


# lst3 = []
# lst3.append(3)
# si = sys.getsizeof(lst3)  # 56 bytes # adds 8 bytes when a new element is added
# print(si)
#
# tup = (3,)
# si = sys.getsizeof(tup)  # 40 bytes # adds 8 bytes when a new element is added
# print(si)

# s = {3, 43, 21}
# si = sys.getsizeof(s)  # 216
# print(si)

# i = 2
# print(sys.getsizeof(i))
#
# a = "Hello hi"
# # print(list(a))
# b = list(a)
# b[1]="b"
# print(b[1])
# print(b)

# l = ('b', 'a', 'a', 'ba', 'ab', 12)
# sorted(l)
# print(l)


# l = [1, 2, 3, 4]
# it = iter(l)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))


# def gener_sam(n):
#     for i in range(1, n + 1):
#         yield i * i


# a = gener_sam(10)
# print(next(a))
#
# print(next(a))
