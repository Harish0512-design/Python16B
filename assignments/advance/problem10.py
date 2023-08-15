# 10)Define a function that will take two positional arguments and
# one default argument. And print sum of those arguments.

def calculate_sum(a, b, c=5):
    return a + b + c


# print(calculate_sum(3, 4))
if __name__ == "__main__":
    a, b = tuple([int(input("Enter value: ")) for x in range(2)])  # unpacking
    print(calculate_sum(a, b))
    res = [int(input("Enter value: ")) for x in range(2)]
    print(calculate_sum(res[0], res[1]))
