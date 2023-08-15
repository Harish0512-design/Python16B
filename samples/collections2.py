# list data type
# ------------------

# list creation :- lst = [2,34,5] or using list()


# lst = [1, 2, 3, "John", True, 12.5]

# built-in methods

# 1.
# lst.pop()
# removes last element and returns it, raises index error if list is empty

# lst.pop(3)
# removes element at specified index and returns it,
# raises index error if index out of range or list is empty

# 2.
# lst.append(4)
# adds element at the end of list and returns None

# 3.
# lst.clear()
# removes all the elements from the list, returns None

# 4.
# lst.index(3)
# returns the index of given number, raises value error if value is not available

# 5.
# lst.insert(idx, ele)
# inserts element at specific index, returns None

# 6.
# lst.count(3)
# counts no. of occurrences of a specific element in list

# 7.
# lst.extend(iterable))
# adds all the elements in iterable(list, set, tuple, dict(only keys will be taken by default))
# to lst at the end

# 8.
# lst.reverse()
# reverse a list, returns None

# 9.
# lst2 = lst.copy()
# Return a shallow copy of the list.

# aliasing vs cloning:
# -----------------------
# the process of providing another reference variable to the list is called aliasing.
# if u change any value using reference variable then the original list also gets modified

# to overcome this problem we should go for cloning
# The process of creating exactly duplicate independent object is called Cloning.
# we use copy() to perform cloning


# 10
# removes the first occurrence of value, raises value error if value not present in list
# lst.remove()


# 11.
# lst.sort()

# ascending order by default
# sort the elements in ascending order (numbers, alphabets (order:- ['1', '2', 'A','B','a', 'b'],
# boolean(order:- [False, True, True])))
# by default follows ASCIIbetical order

# if elements in list are of different data types then sort() doesn't work.
# raises TypeError: '<' not supported between instances of 'str/int/NoneType' and 'int/str/NoneType'

# if u want to sort lower case first and then upper case then u can use custom function as key

# descending order
# lst = [1,3,4,5]
# lst.sort(reverse=True)

# difference between sort() and sorted() function
# ------------------------------------------------------------------------------------------------

# sort() and sorted() are used to achieve the same task but
# the sort() method doesn’t return anything, it modifies the original list.
# If you don’t want to modify the original list, use sorted() function. It returns a sorted copy of the list.
# Another difference is that the sort() method is only defined for lists.
# the sorted() function accepts any iterable like tuple, dictionary etc.
# Also, the sort() method doesn’t need to create a new list, so it’s faster.

# lst3 = ['b', 'd', 'c', 'h', 'i', 'j', 'a', 'z']
# print(lst3)
# lst3.sort()
# print(lst3)     # ['a', 'b', 'c', 'd', 'h', 'i', 'j', 'z']


# upper case first, followed by lowercase (using ASCII values)

# lst4 = ['bac', 'ade', 'ace', 'Harish', 'India', 'mnjK', 'a', 'z']
# print(lst4)
# lst4.sort()
# print(lst4)    # ['Harish', 'India', 'a', 'ace', 'ade', 'bac', 'mnjK', 'z']


# num chars followed by upper case , lowercase
# lst5 = ['1', '2', 'a', 'b', 'c', 'A', '7000000']
# lst5.sort()
# print(lst5)   # ['1', '2', '7000000', 'A', 'a', 'b', 'c']

# will get type error '<' not supported for str and int. True: 1, False: 0
# lst6 = [True, 12, 'abc']
# lst6.sort()
# print(lst6)


# lst7 = [None, None]
# # TypeError: '<' not supported between instances of 'NoneType' and 'NoneType'
# lst7.sort()
# print(lst7)

# sorting boolean values False 0 , True 1
# lst8 = [True, False, True, True]
# lst8.sort()
# print(lst8) # [False, True, True, True]

# descending order
# lst = [1, 2, 3, 5]
# lst.sort(reverse=True)
# print(lst)


# sorting a list with lowercase letters first and upper case letters next
#
# def custom_funct(val):
#     if val.islower():
#         return 0, val
#     else:
#         return 1, val
#
#
# lst = ['a', 'A', 'B', "HARISH", 'harish']
# print(lst)
# lst.sort(key=lambda s: custom_funct(s))
# print(lst)


# I want to sort strings according to its length

# lst = ['abcdef', 'bac', 'a', 'b']
# lst.sort(key=len)
# print(lst)  # ['a', 'b', 'bac', 'abcdef']


# I want to sort according to the ages

# lst = [('Chandan', 25), ('Krishna', 45), ('John', 20)]
# lst.sort()
# print(lst) # [('Chandan', 25), ('John', 20), ('Krishna', 45)]
# lst.sort(key=lambda t:t[1])
# print(lst) # [('John', 20), ('Chandan', 25), ('Krishna', 45)]


# I want to sort according to the key, values (dictionary)

# lst = [{'Name': 'Chandan', 'age': 25}, {'Name': 'Krishna', 'age': 45}, {'Name': 'John', 'age': 20}]
# lst.sort(key=lambda d:d['Name'])
# print(lst)
# output : [{'Name': 'Chandan', 'age': 25}, {'Name': 'John', 'age': 20}, {'Name': 'Krishna', 'age': 45}]

# lst.sort(key=lambda d: d['age'])
# print(lst)
# output
# [{'Name': 'John', 'age': 20}, {'Name': 'Chandan', 'age': 25}, {'Name': 'Krishna', 'age': 45}]


# lst = [{'Chandan': 24}, {'Krishna': 45}, {'John': 35}]
# lst.sort() # TypeError: '<' not supported between instances of 'dict' and 'dict'


# list comprehension :
# l = [x * x for x in range(1, 11)]
# print(l)

# concatenation and repetition in lists

# lst1 = [1, 2, 3]
# lst2 = [3, 4, 5]
# lst1 = lst1 + lst2 # [1, 2, 3, 3, 4, 5]
# print(lst1)

# lst1 = lst1 * lst2  # TypeError: can't multiply sequence by non-int of type 'list'
# lst1 = lst1 - lst2  # TypeError: unsupported operand type(s) for -: 'list' and 'list'
# lst1 = lst1 * 3     # [1, 2, 3, 1, 2, 3, 1, 2, 3]
# print(lst1)


# -----------------------------------------------------------------------------------------------------

# adds an element at last and returns NONE
# lst.append(45)
# print(lst)

# inserts an element at specified index and returns None
# insert(index, value_to_insert)
# lst.insert(2, 3)
# print(lst)

# removes the last element and returns the removed element, raises index error
# print(lst.pop())

# removes the element at a specified index and returns the removed element, raises index error if index not present
# print(lst.pop(3))

# removes the first occurrence of value, raises value error if value not present in list
# print(lst)
# lst.remove(3)
# print(lst)

# returns the index of given value(element)
# print(lst.index(2))
#
# print(lst)
# removes all the elements in the list
# lst.clear()
# print(lst)

# adding dictionary keys. by default, dict has iter() method which iterates over keys

# lst = [3, 4, 5, 6]
# lst.extend({1: 2, 2: 3, 4: 5, 6: 7})

# print(lst)

# lst.extend({1, 2, 3, 4})  # set
# lst.extend((1, 2, 3, 4))  # tuple
# lst.extend([1, 2, 3, 4])  # list

# print(lst)
#
# lst.reverse()
# print(lst)
# lst = [1, 2, 3, 4]
# print(lst[::-1])

# lst2 = lst.copy()
# print(lst2)
# lst2.sort()
# print(lst2)


# Tuple data type
# ------------------------------------------------------------------

# tuple creation : (1,23,4,5)
# tup1 =   ()
# print(tup1)
# print(type(tup1))
# tup = (1,)        # creating tuple with single value (,) is mandatory


# tup = (1)         # this will not create tuple instead it creates integer
# print(type(tup)) # <class 'int'>

# tup = ('abc')
# print(type(tup)) # <class 'str'>


# # packing : The process of combining multiple elements into a single tuple
# t = 1, 2, 3, 5
# print(t)
#

# # unpacking : The process of extracting elements from a tuple and assigning them to different variables
# a, b, c, d = t
# print(a)
# print(b)
# print(c)
# print(d)


# # *b (remaining values in tuple assigned to variable b)
# a, e,*b, z = (3, 4, 5, 2922, 39393)
# print(a)  # 3
# print(b)  # (4, 5, 2922)
# print(z)  # 39393

# a, *b, z, *k = (3, 4, 5, 2922, 39393)  # SyntaxError: two starred expressions in assignment


# tup = tuple('Geeks for geeks')      # ('G', 'e', 'e', 'k', 's', ' ', 'f', 'o', 'r', ' ', 'g', 'e', 'e', 'k', 's')
# print(tup)
# tup = tuple(None)   # TypeError: 'NoneType' object is not iterable


# built-in methods
# --------------------------------


# tup = (1, 2, 4, 2, 7, 8, 9)

# 1. count()
# returns no. of occurrences of a given number
# print(tup.count(2))

# 2. index()
# returns the index position of the given element
# print(tup.index(2))


# tuple comprehension
# -------------------------
# It is not possible because it internally generates a generator object

# tup1 = (x ** 2 for x in range(1, 10))
# print(tup1)  # <generator object <genexpr> at 0x000001BE10F3EBA0>


# tuple concatenation and repetition
# --------------------------------------

# tup1 = (2, 3, 4, 4)
# tup2 = (3, 42, 1, 39, 92)
#
# tup_concat = tup1 + tup2  # creates a new tuple object because tuple is immutable
# print(tup_concat)
#
# tup_repeat = tup1 * 2  # creates a new tuple object
# print(tup_repeat)
#
# print(id(tup1))  # 1730508917872
# print(id(tup_repeat))  # 1730508896512
# print(id(tup_concat))  # 1730508770992


# set
# ------------------------------------------------------------------------------------------

# set creation

# s = {1,2,3,4} or using set() function

# s = {}  # internally creates a dictionary by default not a set
# s = set()
# s = {1, 2, 3, 4, 5, 6, 6, 6, 3}
# print(s)

# built-in methods
# ---------------------------------------------

# 1. add() :
# adds element to the set, returns None

# s.add(8)
# print(s)

# 2. remove() :
# removes element from the set, raises 'KeyError' if value is not present in the set, returns None


# s.remove(78)
# print(s)

# 3. discard() :
# removes element from the set, do not raise 'KeyError' if value is not present in the set, returns None

# s = {1, 3, 4, 5}
# s.discard(78)
# print(s)

# 4. pop() :
# removes a random element and returns it, raises KeyError if set is empty
#
# s1 = {5, 12, 100}
# t = s1.pop()
# print(t)
# print(s1)

# 5. clear() :
# removes all the elements from the set and returns None

# s = {'harish', 'Harish'}
# print(s)
# s.clear()
# print(s)


# 6. copy():
# returns exact copy of the set

# s = {'abc', 1, 2, 3}
# k = s.copy()
# k.add(5)
# print(s)
# print(id(s))
# print(id(k))


# 7. union():
# returns all the elements (if element present twice or thrice returns only once)

# s1 = {1, 3, 4, 5, 8}
# s2 = {3, 4, 5, 6}
# union_set = s1.union(s2)
# print(union_set)

# 8. intersection()
# returns common elements from both sets

# s1 = {1, 3, 4, 5, 8}
# s2 = {3, 4, 5, 6}
# intersection_set = s1.intersection(s2)
# print(intersection_set)


# 9. difference()
# returns only unique values in set 1

# s1 = {1, 3, 4, 5, 8}
# s2 = {3, 4, 5, 6}
# diff_set = s1.difference(s2)
# print(diff_set)


# 10. symmetric_difference()
# returns elements present in set 1 or set2 but not in both

# s1 = {1, 3, 4, 5, 8}
# s2 = {3, 4, 5, 6}
# sym_diff = s2.symmetric_difference(s1)
# print(sym_diff)


# 11. issubset()
# returns True/False if all the elements of subset are in superset

# s1 = {1, 2, 3, 4, 5, 6, 7}
# s2 = {3, 4, 5, 6}
#
# print(s2.issuperset(s1))


# 12. issuperset()
# returns True/ False if all the elements of subset are in superset

# s1 = {1, 2, 3, 4, 5, 6, 7, None, 'Harish'}
# s2 = {3, 4, 5}
#
# print(s1.issuperset(s2))

#
# s1 = {1, 2, 3, 4, 5, 6, 7, None}
# s2 = {None}
#
# print(s1.issuperset(s2))


# set comprehension is possible

# s={2**x for x in range(2,10,2)}
# print(s) #{16, 256, 64, 4}


# dictionaries
# -------------------------------------------------------------------------------------------

# dictionary creation: d=dict() or d = {}
d = {}  # empty

# adding entries
# d[100] = "ram"
# d[200] = "ravi"
# d[300] = "shiva"
# print(d)  # {100: 'ram', 200: 'ravi', 300: 'shiva'}

# creating dict with values
# d = {100: 'ram', 200: 'ravi', 300: 'shiva'}

# creating dict using dict() method with list of tuples as key-value pairs
# d = dict([(100, "ram"), (200, "shiva"), (300, "ravi")])

# accessing dict values
# print(d[100])     # raises KeyError if key is not present in the dictionary

# dict in-built methods
# -------------------------------
# 1.
print(d.values())

# 2.
print(d.keys())

# 3
print(d.items())

# 4
d2 = {
    400: 'Raju',
    500: 'Ganesh'
}
d.update(d2)

# 5
print(d.pop(400))

# 6
print(d.get(500))  # returns value of given key, if key not found then it will returns None
print(d.get(800, 'Key not found'))  # returns value of a given key, if key not found it will return default msg.

# 7
print(d.clear())

# 8
print(d.popitem())

# comprehensions
lst = [1, 2, 3, 4, 5]


# lst1 = []
# for i in range(1, 100):
#     lst1.append(i)
# print(lst1)
# lst1 = {i for i in range(1, 100) if i % 2 == 0}
# print(lst1)

# l1 = ['name', 'age', 'course']
# l2 = ['chaitanya', 23, 'Python']
#
# d = {k: v for k, v in zip(l1, l2)}
#
# # for i in range(1, 101):
# #     d[i] = i**2
# print(d)
#
# d = {
#     'name': 'chaitanya',
#     'age': 23,
#     'course': 'python'
# }
#
# d1 = {
#
# }
#
# k = d.keys()  # ['name', 'age', 'course']
# v = ['phani2', 23, 'python']
# for key, val in zip(k, v):
#     d1[key] = val
# print(d1)

#
# def add(*a):
#     sum_of_numbers = 0
#     for i in a:
#         sum_of_numbers += i
#     print(sum_of_numbers)


# add(2)
# add(2,3)
# add(1,3,4,5,5,6,7,7)

