# Create an Arithmetic class that has functions for addition, subtraction create one more
# class Calculator which have multiplication, division
# now inherit the class Arithmetic into Calculator and access all the methods.

class Arithmetic:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return self.num1 + self.num2

    def subtraction(self):
        return self.num1 - self.num2


class Calculator(Arithmetic):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def multiplication(self):
        return self.num1 * self.num2

    def addition(self):
        return self.num1 + self.num2

    def subtraction(self):
        return self.num1 - self.num2

    def division(self):
        return self.num1 / self.num2


res = Calculator(12, 2)
print(res.multiplication())
print(res.addition())
res.num1 = 23
res.num2 = 3
print(res.division())
print(res.subtraction())
