# 18)Program to execute pre-defined exceptions?

def index_error(lst):
    return lst[len(lst)]


def file_not_found(file):
    with open(file, 'r') as f:
        return f.read()


def key_error(s_dict):
    return s_dict['key']


def zero_division_error(num1):
    return num1 // 0


def value_error(no_in_str):
    return int(no_in_str)


try:
    index_error([1, 2, 3])
except IndexError as e:
    print("index error out of range  == ", e)

try:
    file_not_found("file4.txt")
except FileNotFoundError as e:
    print("File not found at the directory == ", e)

try:
    zero_division_error(45)
except ZeroDivisionError as e:
    print("Zero division error == ", e)

try:
    value_error('123s')
except ValueError as e:
    print("Value Error == ", e)

try:
    key_error({'name': 'Harish'})
except KeyError as e:
    print("Key error == ", e)
