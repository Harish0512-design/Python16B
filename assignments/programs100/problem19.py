# You are required to write a program to sort the (name, age, height)
# tuples by ascending order where name is string, age and height are
# numbers. The tuples are input by console. The sort criteria is:
# 1: Sort based on name;
# 2: Then sort based on age;
# 3: Then sort by score.
# The priority is that name > age > score.
# If the following tuples are given as input to the program:
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'),
# ('Json', '21', '85'), ('Tom', '19', '80')]
# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.
# We use itemgetter to enable multiple sort keys.

# from operator import itemgetter
#
# l = []
# while True:
#     s = input()
#     if not s:
#         break
#     l.append(tuple(s.split(",")))
# print(sorted(l, key=itemgetter(0, 1, 2)))

# d = {
#     100 : 1200,
#     200: 1300
# }
#
# print(sorted(d.items(), reverse=True))
def max_profit(prices):
    if len(prices) < 2:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit

    return max_profit


prices = [7, 1, 5, 3, 6, 4]
result = max_profit(prices)
print(result)