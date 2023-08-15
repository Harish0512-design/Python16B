# data = "index error out of range  ==  list index out of range\n" \
#        "File not found at the directory ==  [Errno 2] No such file or directory: 'file4.txt' \n" \
#        "Zero division error ==  integer division or modulo by zero\n" \
#        "Value Error ==  invalid literal for int() with base 10: '123s'"
# with open('sample.txt', 'w') as f:
#     f.write(data)
#
with open('sample.txt', 'r') as f:
    # print(f.read())
    # reads only the one line at a time
    # print(f.readline())
    # returns a list by separating each line as a list item
    print(f.readlines())

# with open('sample.txt', 'a', encoding='utf-16') as f:
#     f.write('El Niño')
