# class CreditCard:
#     def __init__(self, card_no, balance):
#         self.card_no = card_no
#         self.balance = balance
#
#
# class Customer:
#     def __init__(self, cards):
#         self.cards = cards
#
#     def purchase_item(self, price, card_no):
#         if price < 0:
#             raise Exception()
#         if card_no not in self.cards:
#             raise Exception()
#         if price > self.cards[card_no].balance:
#             raise Exception()
#
#
# card1 = CreditCard(101, 800)
# card2 = CreditCard(102, 2000)
# cards = {card1.card_no: card1, card2.card_no: card2}
# c = Customer(cards)
# while (True):
#     card_no = int(input("Please enter a card number"))
#     try:
#         c.purchase_item(1200, card_no)
#         break
#     except Exception as e:
#         print("Something went wrong. " + str(e))

#
# try:
#     x = int(input("enter 1st number "))
#     y = input("enter 2nd number ")
#     s = x / y
# except TypeError as e:
#     print(e)
# finally:
#     print(" Completed ")


# def foo():
#     try:
#         raise ZeroDivisionError
#         print(1)
#     finally:
#         print(2)
#
# # print(foo())
# foo()

#
# try:
#     if '1' != 1:
#         raise "someError"
#     else:
#         print("Some error not occured")
# except 'someError':
#     print("Some error occured")


# try:
#     n = int(input("Enter a number"))
#     m = int(input('Enter another number'))
#     x = n/m
# except ZeroDivisionError:
#     print("Zero Division Error")
# except:
#     print("Some error occured")
# else:
#     print("Else part")
# finally:
#     print("Finally block")

#
# try:
#     raise
# except ZeroDivisionError:
#     print("Zero division error")
# except:
#     print("re raise")


# try:
#     f = open(r"d:\hi.txt", 'r')
#     f.read()


# except FileNotFoundError as e:
#     print("File not found Error == ", e)
#
# except IOError as e:
#     print("IO Error == ", e)
#
# except OSError as e:
#     print("OS Error == ", e)
# except:
#     print("Default exception")
# finally:
#     print("completed")

# class NotEnoughBalance(Exception):
#     pass
#
#
# try:
#     amount = float(input("Enter the amount to withdraw "))
#     if amount > 50000:
#         raise NotEnoughBalance
#     else:
#         print("Money withdrawal successfully")
# except NotEnoughBalance as e:
#     # print(type(e).__name__)
#     print("Not enough Balance")
# finally:
#     print("Please visit again..")


# class InvalidAcNo(Exception):
#     pass
#
#
# def get_ac_bal(ac_no):
#     if ac_no > 0:
#         print(ac_no)
#     else:
#         raise InvalidAcNo("Invalid account number")
#
# try:
#     get_ac_bal(0)
# except InvalidAcNo as e:
#     print(e)
# finally:
#     print("Visit again...")

# try:
#     raise
# except ZeroDivisionError:
#     print("Error")
# except Exception as e:
#     print("Default error", e)

# class CreditCard:
#     def __init__(self, card_no, balance):
#         self.card_no = card_no
#         self.balance = balance
#
#
# class Customer:
#     def __init__(self, cards):
#         self.cards = cards
#
#     def purchase_item(self, price, card_no):
#         if price < 0:
#             raise Exception()
#         if card_no not in self.cards:
#             raise Exception()
#         if price > self.cards[card_no].balance:
#             raise Exception()
#
#
# card1 = CreditCard(101, 800)
# card2 = CreditCard(102, 2000)
# cards = {card1.card_no: card1, card2.card_no: card2}
# c = Customer(cards)
# while (True):
#     card_no = int(input("Please enter a card number"))
#     try:
#         c.purchase_item(1200, card_no)
#         break
#     except Exception as e:
#         print("Something went wrong. " + str(e))


# ZeroDivisionError

# name = "hi how r you guys"
#
# lst = sorted(name.split(' '), key=len)
# print("min ", lst[0])
# print("max ", lst[-1])

#
# def funct(a, b):
#     sum = a+b
#     continue
#     print(sum)

# #
# def funct(l):
#     #     # l = l * 5
#     print(id(l))
#     for i in range(len(l)):
#         l[i] = 5 * l[i]
#     print(id(l[0]))
#
#
# #
# #
# l = [1, 2, 3, 4]
# print(id(l[0]))
# ans = funct(l)
# print(ans)
# print(l)

# def func(l):
#     l = 5 * l
#     print(l)


# l = 6
# ans = func(l)
# print(ans)
# print(l)

# def func(dic):
#     dic.update({'name': 'harish', 'course': 'aws'})
#     return dic
#
#
# d = {
#     'python3': 'python, django, sqllite3',
#     'db': 'mysql'
# }
# print(func(d))
# print(d)
#
# def fun(s):
#     print(id(s))
#     s.add(5)
#
# s = {1, 3, 4}
# print(id(s))
# fun(s)
# print(s)
#
# l = [i for i in range(10000000)]
# t = (i for i in range(10000000))
#
# import time
#
# st = time.time()
# t = 0
# for i in l:
#     t += i
# et = time.time()
# print(et - st)
#
# st = time.time()
# t = 0
# for i in t:
#     t += i
# et = time.time()
# print(et - st)

# def func(a, b):
#     a = a + b
#     pass
#     return a
#
#
# print(func(3, 4))
# i = 5
# while i > 0:
#     print(i)

# from sample_class import MyClass
#
# try:
#     MyClass.to_add()
# except ImportError as e:
#     print("Import Error occurred ", e)
#
# import json
# import pandas as pd
#
# def lambda_handler(event, context):
#     return {
#         'statusCode': 200,
#         'body': json.dumps('Hello')
#     }
