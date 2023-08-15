# l = ['1', '12', '123', '1234']
# for i in range(len(l)):
#     l[i] = l[i].zfill(10)
# print(l)

# import time


# for i in range(len(l)):
#     if len(l[i]) < 10:
#         l[i] = '0' * (10 - len(l[i])) + l[i]
# print(l)

from typing import List

#
# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         n = len(matrix)
#
#         # Step 1: Transpose the matrix
#         for i in range(n):
#             for j in range(i, n):
#                 matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
#
#         # Step 2: Reverse each row of the transposed matrix
#         for i in range(n):
#             matrix[i] = matrix[i][::-1]


# for i in range(len(account_list)):
#     if len(account_list) > 10:
#         return False
#     else:
#         len(account_list) < 10
#         len(account_list - 10) * 0
#     print(account_list)

input_list = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
res_list = []
# print(input_list)
for li in input_list:
    print(li)
print("="*40)
for i in range(len(input_list)):
    # print(input_list[i])
    new_list = [input_list[0][i], input_list[1][i], input_list[2][i]]
    res_list.append(new_list[::-1])
# print(res_list)

import time
print(time.strftime("%H:%M:%S"))

for l in res_list:
    print(l)
