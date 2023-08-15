# Write a program which accepts a string as input to print "Yes" if the
# string is "yes" or "YES" or "Yes", otherwise print "No".
# Hints:
# Use if statement to judge condition.

# input_val = input()
# if input_val.lower() == 'yes':
#     print("Yes")
# else:
#     print("No")

input_val = input()
if input_val == 'Yes' or input_val == 'yes' or input_val == 'YES':
    print("Yes")
else:
    print("No")
