# 8. Write a function to check if a number is even or not.
def check_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


res = check_even_or_odd(23)
print(res)
