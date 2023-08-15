# Define a function which can print a dictionary where the keys are
# numbers between 1 and 3 (both included) and the values are square of
# keys.
# Hints:
# Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number.

# def get_squares(limit):
#     square_dict = {}
#     for i in range(1, limit + 1):
#         square_dict[i] = i ** 2
#
#     return square_dict
#
#
# print(get_squares(3))
# print(get_squares(200))

def print_dict():
    d = dict()
    d[1] = 1
    d[2] = 2 ** 2
    d[3] = 3 ** 2
    print(d)


print_dict()
