# 1: Convert two lists into a dictionary

# keys = ['emp_id', 'emp_name', 'emp_doj', 'emp_salary']
# values = ['e1001', 'John', '02-11-2021', '45000']

# way-1
# emp = {}
# for k, v in zip(keys, values):
#     emp[k] = v
#
# print(emp)

# way-2
# emp = dict(zip(keys, values))
# print(emp)

# way-3
# emp = {}
# for i in range(len(keys)):
#     emp[keys[i]] = values[i]
# print(emp)

# way-4
# emp = {k: v for k, v in zip(keys, values)}
# print(emp)


# 2: Merge two Python dictionaries into one

# person = {
#     'name': 'John',
#     'age': 14
# }
# std = {
#     'std': 10,
#     'school': 'svu'
# }
# person.update(std)
# print(person)

# 3: Print the value of key ‘history’ from the below dict

# marks = {
#     'civics': 20,
#     'history': 23,
#     'geography': 22,
#     'economics': 23
# }
# print(marks['history'])


# 4: Initialize dictionary with default values

# d = {
#     'civics': 20,
#     'history': 23,
#     'geography': 22,
#     'economics': 23
# }
#
# # 5: Create a dictionary by extracting the keys from a given dictionary
# existing_dict = {
#     'name': 'John',
#     'doj': '12/12/2018',
#     'salary': 23000
# }
# print(existing_dict)
# new_dict = {k: v for k, v in zip(existing_dict.keys(), ['James', '12/11/2019', 25000])}
# print(new_dict)


# 6: Delete a list of keys from a dictionary

# existing_dict = {
#     'name': 'John',
#     'doj': '12/12/2018',
#     'salary': 23000
# }
# key_lst = ['doj', 'salary']
# for k in key_lst:
#     if k in existing_dict.keys():
#         existing_dict.pop(k)
# print(existing_dict)

# 7: Check if a value exists in a dictionary

# existing_dict = {
#     'name': 'John',
#     'doj': '12/12/2018',
#     'salary': 23000
# }
#
# if 'name' in existing_dict.keys():
#     print(existing_dict['name'])
# print(existing_dict)

# 8: Rename key of a dictionary

# existing_dict = {
#     'name': 'John',
#     'doj': '12/12/2018',
#     'salary': 23000
# }
# existing_dict['full_name'] = existing_dict.pop('name')
# print(existing_dict)

# 9: Get the key of a minimum value from the following dictionary

# marks = {
#     'maths': 90,
#     'science': 86,
#     'ps': 86,
#     'social': 89
# }
# keys = []
# min_value = min(marks.values())
# for k in marks.keys():
#     if marks[k] == min_value:
#         keys.append(k)
# print(min_value)
# print(keys)

# 10: Change value of a key in a nested dictionary

# flights = {
#     'Air-India': {
#         'departure': 'Delhi',
#         'destination': 'Bangalore'
#     },
#     'Indigo': {
#         'departure': 'Bangalore',
#         'destination': 'Hyderabad'
#     }
# }
#
# flights['Indigo']['origin'] = flights['Indigo'].pop('departure')
#
# print(flights)

# 1: Create a function with variable length of arguments

# def add(*args):
#     addition = 0
#     for i in args:
#         addition += i
#     return addition
#
#
# print(add(1, 2, 3, 4, 5))
# print(add(1, 2, 3))
# print(add(1, 2, 3, 4, 5, 6, 7, 9))

# 2: Return multiple values from a function
# def greetings():
#     return "Good morning", "Good afternoon", "Good evening"


# 3: Create a function with a default argument
# def sub(num1, num2=5):
#     return num1 - num2


# print(sub(10))

# 4: Create an inner function to calculate the addition in the following way

# def outer(a, b):
#     def inner(num1, num2):
#         return num1 + num2
#
#     return inner(a, b)
#
# res = outer(3, 4)
# print(res)

# 5 : Assign a different name to function and call it through the new name
# def fun1():
#     return "hello"
#
#
# print(fun1())
# f1 = fun1()
# print(f1)

# 6: Generate a Python list of all the even numbers between 4 to 30

# even_list = [x for x in range(4, 31) if x % 2 == 0]
# print(even_list)

# 7: Find the largest item from a given list
# lst = [1, 12, 60, 34, 20, 14, 9]
# print(max(lst))
# max_number = lst[0]
# for i in lst:
#     if i > max_number:
#         max_number = i
# print(max_number)
