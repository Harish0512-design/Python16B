# Please write assert statements to verify that every number in the list
# [2,4,6,8] is even.
# Hints:
# Use "assert expression" to make assertion.
# even_num_lst = [2, 4,5, 6, 8, 9]
even_num_lst = [2, 4, 6, 8]
for i in even_num_lst:
    assert i % 2 == 0, "Not a even number"
