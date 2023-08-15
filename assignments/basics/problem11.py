# Write a function that returns the maximum of two numbers.
def max_two_numbers(num1, num2):
    return num1 if num1 > num2 else num2


if __name__ == "__main__":
    print(max_two_numbers(2, 54))
    print(max_two_numbers(3, 1))
    print(max_two_numbers(-9, 0))
    print(max_two_numbers('a', 'b'))
