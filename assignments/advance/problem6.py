# 6) Write a Python program to multiply all the items in a dictionary

def multiply_items(dict_sample):
    res = 1
    for v in dict_sample.values():
        res *= v
    return res


print(multiply_items({'a': 1, 'b': 12, 'c': 12}))
