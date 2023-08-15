# 5)Write a Python program to convert a list into a dictionary where keys are the
# unique elements of the list and the values are their frequency.
# Ex:
# Input: ['a', 'b', 'c', 'a', 'd', 'e']
# Output: {'a': 2, 'b': 1, 'c': 1, 'd': 1, 'e': 1}

def lst_to_dict_convertor(lst):
    res_dic = {}
    for i in lst:
        if i not in res_dic.keys():
            res_dic[i] = lst.count(i)
    return res_dic


print(lst_to_dict_convertor(['a', 'b', 'c', 'a', 'd', 'e']))
