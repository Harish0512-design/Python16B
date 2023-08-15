# Define a function that can accept two strings as input and print the
# string with maximum length in console. If two strings have the same
# length, then the function should print all strings line by line.
# Hints:
# Use len() function to get the length of a string

def string_with_max_length(str1, str2):
    l1 = len(str1)
    l2 = len(str2)
    if l1 > l2:
        print(str1)
    elif l1 == l2:
        print(str1)
        print(str2)
    else:
        print(str2)


string_with_max_length('Python', 'Django')
string_with_max_length('Python', 'SQL')
string_with_max_length('Aws', 'Azure')
