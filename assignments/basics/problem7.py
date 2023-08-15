# 7.Write a function “perfect()” that determines if parameter number is a perfect number.
# Use this function in a program that determines and prints all the perfect numbers between 1 and 1000.
#
# [An integer number is said to be “perfect number” if its factors,
# including 1(but not the number itself), sum to the number. E.g., 6 is a perfect number because 6=1+2+3].

def perfect(val):
    count = 1
    for i in range(2, val):
        if val % i == 0:
            count += i
    if count == val:
        print(val, end=",")


for i in range(1,1000):
    perfect(i)