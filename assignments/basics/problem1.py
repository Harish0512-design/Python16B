# 1.Print multiplication table of 12 using recursion.

def multiply(val, counter):
    if 0 < counter < 11:
        print(f'{val}X{counter} = {val * counter}')
        multiply(val, counter + 1)
    else:
        print(end="")


multiply(14,1)
