# Write a program that computes the value of a+aa+aaa+aaaa with a given
# digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106
# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.

# print(9 + 99 + 999 + 9999)

input_value = input()
res_sum = 0
for i in range(1, 5):
    res_sum += int(input_value * i)
print(res_sum)
