def outer_functions(n):
    def inner_function(m):
        return n - m

    return inner_function


closure_instance = outer_functions(4)
result = closure_instance(5)
print(result)
