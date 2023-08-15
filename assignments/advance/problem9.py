# 9)Read two values using input() and
# find the first value position in the list and replace that with the second value in the list.

# r = [x for x in input()[:2]]
r = list(map(lambda x: int(x), input().split(',')))
r.reverse()
print(r)
