# 4)Write a Python program to count the number of strings where the string length is 2 or more and
# the first and the last characters are the same from a given list of strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result: 2

def get_string_count(lst):
    count = 0
    for e in lst:
        if len(e) >= 2 and e[0] == e[-1]:
            count += 1
    return count


print(get_string_count(['abc', 'xyz', 'aba', '1221']))
