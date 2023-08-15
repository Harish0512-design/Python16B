# Write a program to compute the frequency of the words from the input.
# The output should output after sorting the key alphanumerically.
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1
# Hints
# In case of input data being supplied to the question, it should be
# assumed to be a console input.


input_val = input().split()
# converting list to set to remove duplicates
input_val_to_set = set(input_val)
# sorting the set and it returns a list
set_sorted_to_list = sorted(input_val_to_set)

for val in set_sorted_to_list:
    print(val, ":", input_val.count(val))
