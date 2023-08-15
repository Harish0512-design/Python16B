# Given a string, write a python function to return True if the strings "mat" and "jet"
# appear the same number of times in the given string, else return False.
#
# Note: Perform case insensitive string comparison wherever necessary.

# Sample Input                                Expected Output
# Jet on the Mat but mat is too long             False
# mat jet Jet Mat                                True
#
# def add(a, b):
#     return a + b
#
#
# print(add(4, 5))
#
# add = lambda a, b: a + b
# print(add(4, 5))


def check_string_count(str_value):
    mat_count = str_value.lower().count("mat")
    jet_count = str_value.lower().count("jet")
    if mat_count == jet_count:
        return True
    else:
        return False


if __name__ == "__main__":
    res1 = check_string_count("Jet on the Mat but mat is too long")
    print(res1)
    res2 = check_string_count("mat jet Jet Mat")
    print(res2)
print("harish", "Reddy", "Phani", sep='*****')


# Write a Python function which accepts a string and returns a string made of the first 2 and the last 2 characters
# of the given string
# If the string length is less than 2, return -1.
#
# Note: If the string length is equal to 2, consider the 2 characters to be the first as well as the last two characters.

def print_string_ends(str_value):
    if len(str_value) < 2:
        return -1
    elif len(str_value) == 2:
        return str_value
    else:
        return str_value[0:2] + str_value[-2:]


print(print_string_ends("Hello"))
print(print_string_ends("He"))
print(print_string_ends("H"))
