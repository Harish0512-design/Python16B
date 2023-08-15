# 14. Write a program to demonstrate multiple and multi-level inheritances by using the above defined classes.
from assignments.advance.problem12 import Calculator, Arithmetic
from assignments.advance.problem13 import FloorDivision


class MultiLevelInheritanceImpl(Calculator):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def exponential(self):
        return self.num1 ** self.num2


class MultipleInheritance(Arithmetic, Calculator, FloorDivision):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def exponential(self):
        return self.num1 ** self.num2


res = MultipleInheritance(2, 3)
print(res.addition())
print(res.multiplication())
print(res.subtraction())
print(res.floor_division())
