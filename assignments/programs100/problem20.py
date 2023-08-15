# Define a class with a generator which can iterate the numbers, which
# are divisible by 7, between a given range 0 and n.
# Hints:
# Consider use yield

def generator_func(n):
    for i in range(1, n + 1):
        if i % 7 == 0:
            yield i


r = generator_func(35)
print(next(r))
print(next(r))
print(next(r))
print(next(r))
,