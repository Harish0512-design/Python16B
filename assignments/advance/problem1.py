# 1) Write a Python program to count the number of characters (character frequency) in a string
# Sample String: google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

def count_chars(value):
    """ case sensitive """
    frequency_count = {}
    str_tup = tuple(value)
    for ch in value:
        if ch not in frequency_count.keys():
            frequency_count[ch] = str_tup.count(ch)
    return frequency_count


print(count_chars("google.com"))
print(count_chars("Harish"))
