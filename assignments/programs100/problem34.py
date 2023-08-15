# Define a function which can generate a dictionary where the keys are
# numbers between 1 and 20 (both included) and the values are square of
# keys. The function should just print the values only.
# Hints:
# Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number.
# Use range() for loops.
# Use keys() to iterate keys in the dictionary. Also we can use item()
# to get key/value pairs.

def print_square_dict():
    d = dict()
    for i in range(1, 21):
        d[i] = i ** 2
    #
    # for v in d.values():
    #     print(v)

    # for k in d.keys():
    #     print(k)

    # for k, v in d.items():
    #     print(k, ':', v)

    for k, v in d.items():
        print(v)


print_square_dict()