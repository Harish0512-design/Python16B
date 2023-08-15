# 10.Write a function to find factorial of a number but also store the factorials
# calculated in a dictionary as done in the Fibonacci series example.


def cal_factorial(number):
    fact = 1
    while number > 1:
        fact *= number
        number = number - 1
    return fact


fact_dict = {}
for i in range(0, 10):
    fact_dict[i] = cal_factorial(i)

print(fact_dict)
