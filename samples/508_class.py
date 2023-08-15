# import sys
#
#
# def fun():
#     l = []
#     for i in range(5):
#         l.append(i)
#     return l
#
#
# ans1 = fun()
# print(ans1)
# print(type(ans1))
# print(sys.getsizeof(ans1))
# print(ans1.__sizeof__())
#
#
#
# def gen():
#     for i in range(5):
#         yield i
#
# # generator object is iterable
# ans2 = gen()
# print(ans2)
# print(type(ans2))
# print(sys.getsizeof(ans2))
# print(ans2.__sizeof__())
# # for i in ans2:
# #     print(i)
# print(ans2.__next__())
# print("hi")
# print(ans2.__next__())
# print(ans2.__next__())


# Task-1
# Iterator concept - Generator vs Iterator

# l = [1, 2, 3, 4]
# an = l.sort()
# print(an)
# a = l.clear()
# print(a)
# a = print("Hi")
# print(a)

# name = "Harish0512@"
# ans = sorted(name)
# print(ans)

# # Decorator
# def master(func):
#     def slave(num):
#         if num >= 18:
#             return "Eligible for vote"
#         else:
#             return "Not eligible for vote"
#         return func(num)
#
#     return slave
#
#
# #
# @master
# def vote(age):
#     return "Hello"

# def master(func):
#     print(func)
#
#     def slave(num):
#         print(num)
#         if num >= 18:
#             print("Eligible for vote")
#             num = num + 10
#         else:
#             print("Not eligible for vote")
#         return func(num)
#
#     return slave
#
#
# @master
# def vote(age):
#     print(age)
#
#
# # calling
# # print(vote(23))
# vote(23)
# vote(12)
