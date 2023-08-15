# def generator():
#     for i in range(100000):
#         yield i
#
#
# g = generator()
# for k in g:
#     print(k)


# def solution(matrix):
#     rows = len(matrix)
#     cols = len(matrix[0])
#     total = 0
#     for row in range(rows):
#         for col in range(cols):
#             if row == 0:
#                 total += matrix[row][col]
#             else:
#                 if matrix[0][col] != 0:
#                      if matrix[row - 1][col] != 0:
#                          total += matrix[row][col]
#     return total


# l = [[0, 1, 1, 2],
#      [0, 5, 0, 0],
#      [2, 0, 3, 3]]
# print(solution(l))

# inputArray = ["aba", "aa", "ad", "vcd", "abaa"]
# k = max(inputArray, key=len)
# print(k)

# def solution(s1, s2):
#     count = 0
#     d1 = {}
#     d2 = {}
#     for i in range(len(s1)):
#         ch1 = s1.count(s1[i])
#         ch2 = s2.count(s2[i])
#         if ch1 not in d1:
#             d1[s1[i]] = ch1
#         if ch2 not in d2:
#             d2[s2[i]] = ch2
#     for k in d1:
#         if k in d2:
#             count += min(d1[k], d2[k])
#     return count
#
#
#
# print(solution("aabcc", "adcaa"))

