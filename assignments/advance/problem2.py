# 2)Write a Python program to find the first appearance of the substring 'not' and 'poor' from a
# given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'.
# Return the resulting string.
# Sample String: 'The lyrics is not that poor!' 'The lyrics is poor!'
# Expected Result: 'The lyrics is good!' 'The lyrics is poor!'

sample_string = input("Enter sample String")
idx_num1 = sample_string.index("not")
idx_num2 = sample_string.index("poor")
if idx_num1 < idx_num2:
    res_str = sample_string[:idx_num1] + "good" + sample_string[idx_num2 + 4:]
print(res_str)