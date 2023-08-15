def smart_divide(func):
    def inner(a, b):
        print("I'm going to divides a and b")
        if b == 0:
            print("Can't divide")
        return func(a, b)

    return inner


@smart_divide
def divide(a, b):
    print(a / b)


# divide(3, 0)
