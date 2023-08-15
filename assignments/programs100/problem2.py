# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a
# single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.

def find_factorial(input_number):
    fact = 1
    while input_number > 0:
        fact *= input_number
        input_number = input_number - 1
    return fact


if __name__ == "__main__":
    input_val = int(input("Enter a number"))
    print(find_factorial(input_val))
