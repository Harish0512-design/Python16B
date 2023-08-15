# 13)Create a class that has a method for float division and inherit this class into the above calculator class.
from problem12 import Calculator


class FloorDivision(Calculator):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def floor_division(self):
        return self.num1 // self.num2


res = FloorDivision(5, 2)
print(res.floor_division())

# import gc
# import ctypes
# a = 11
# # print(id(a))
# # # del a
# # print(a)
# # ctypes.cast(140728332724320)
# b = id(a)
# print(b)
# print(ctypes.cast(b, ctypes.py_object).value)
#
# # 140728332724320
#
# x = 5
# y = 5
# z = x
# x = 5+1
#
# # print(type(x))
# print(id(x))
# print(id(y))
# print(id(z))
