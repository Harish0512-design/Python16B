# Define a function that can accept an integer number as input and print
# the "It is an even number" if the number is even, otherwise print "It
# is an odd number".
# Hints:
# Use % operator to check if a number is even or odd.

def check_even_or_odd(number):
    if number % 2 == 0:
        print('It is an even number')
    else:
        print('It is an odd number')


check_even_or_odd(12)
check_even_or_odd(13)