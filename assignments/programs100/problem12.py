# Write a program, which will find all such numbers between 1000 and
# 3000 (both included) such that each digit of the number is an even
# number.
# The numbers obtained should be printed in a comma-separated sequence
# on a single line.
# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.

even_numbers = ['0', '2', '4', '6', '8']
lst = []
for i in range(1000, 3001):
    str_conv = str(i)
    if (str_conv[0] in even_numbers) and (str_conv[1] in even_numbers) and (str_conv[2] in even_numbers) and (str_conv[
                                                                                                                  3] in even_numbers):
        # print(str_conv)
        lst.append(str_conv)
print(','.join(lst))
