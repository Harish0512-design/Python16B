# 11)Define a function with dynamic arguments, keyword arguments and
# update the key word arguments in a dictionary within the function.

def display_args_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)


display_args_kwargs(1, 2, 2, 4, 5, a=1, b=3, c=4)
