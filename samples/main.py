# after 3.10 switch case in python

# weekday = "sunday"
# match weekday:
#     case "monday":
#         print("Its monday")
#     case "sunday":
#         print("Its sunday")
#     case _:
#         print("Default day")


# input_limit = int(input())
# lst = []
#
# # '_' => we don't care about the iterator value, just that it should run some specific number of times
# for _ in range(input_limit):
#     lst.append(int(input()))
# print(min(lst))
#
# while True:
#     print("I'm a looser")


# iterable objects
# lst = [0, 1, 2, 2, 4, 3]
# iterator is an object which contains a countable number of values and it is used to iterate over iterable objects.
# r = iter(lst)
# print(next(r))
# print("++" * 4)
# print(next(r))

# check number is prime or not
# number = int(input())
# if number % 2 == 0:
#     print(number, " Number is even")
# else:
#     print(number, " Number is odd")
#
# # check vote eligiblity
# age = int(input())
# if age > 18:
#     print("Eligible to vote")
# else:
#     print("Not eligible to vote")
#
# # check number
# number = int(input("Enter a positive number"))
# if number >= 1 and number <= 10:
#     print("Number is between 1 and 10 inclusively")
# elif number >= 11 and number <= 20:
#     print("Number is between 11 and 20 inclusively")
# else:
#     print("Number is greater than 20")
#
# # check week day
#
# day = 1
# if day == 1:
#     print("Sunday")
#
# elif day == 2:
#     print("Monday")
#
# elif day == 3:
#     print("Tuesday")
#
# elif day == 4:
#     print("Wednesday")
#
# elif day == 5:
#     print("Thursday")
#
# elif day == 6:
#     print("Friday")
# else:
#     print("Saturday")

#
# # print numbers whose quotient = 1
# for i in range(20, 40):
#     if i % 2 == 1:
#         print(i)
#
# #

#
# name = "Ram"
# if name == "Harish":
#     print("Hi Harish")
# elif name == "Raju":
#     print("Hi Raju")
# elif name == "Phani":
#     print("Hi Phani")
# else:
#     print("I don't know")

#
# l = [x * x for x in range(100000000)]
# print(l)
#
# t = (x * x for x in range(5))
# while True:
#     print(next(t))


# import copy
#
# lst = [[12, 232, 13, 345, 132], [2,4,46,3,21]]
# lst1 = lst.copy()
# print(lst)
#
# lst1[1][1] = 1000
#
# print(lst1)
# print(lst)
#
#
# lst = [[12, 232, 13, 345, 132], [2,4,46,3,21]]
# lst1 = copy.deepcopy(lst)
# print(lst)
#
# lst1[1][1] = 1000
#
# print(lst1)
# print(lst)
#
# x = 48
# try:
#     x.reverse()
# except AttributeError:
#     print("Attribute Error")
# finally:
#     print("Completed")


# deep copy vs shallow copy

# original_list = ['harish', 33, 39,1910]

# x = 10
# if x == 10:
#     print("Hii")
# else:
#     print("Byee")
