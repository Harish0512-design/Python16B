# 7)Write a Python program to get the maximum and minimum value in a dictionary

def get_max_min(dict_sample):
    lst = dict_sample.values()
    print("max: ", max(lst))
    print("min: ", min(lst))


get_max_min({'a': 3, 'b': 5, 'c': 4})

