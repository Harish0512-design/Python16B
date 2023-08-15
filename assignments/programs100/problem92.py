# With a given list [12,24,35,24,88,120,155,88,120,155], write a program
# to print this list after removing all duplicate values with original
# order reserved.
# Hints:
# Use set() to store a number of values without duplicate.

input_lst = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
# print(list(set(input_lst)))


def remove_duplicates(lst):
    output_list = []
    output_set = set()
    for i in lst:
        if i not in output_set:
            output_set.add(i)
            output_list.append(i)
    return output_list


print(remove_duplicates(input_lst))
