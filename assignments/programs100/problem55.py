# Write a function to compute 5/0 and use try/except to catch the
# exceptions.
# Hints:
# Use try/except to catch exceptions.
#
# def exception_test():
#     try:
#         return 5 / 0
#     except ZeroDivisionError as e:
#         return "Number can't be divisible by 0"
#     finally:
#         return "function executed.."
#
#
# print(exception_test())


def throws():
    return 5 / 0


try:
    throws()
except ZeroDivisionError:
    print("division by zero!")
except Exception as err:
    print('Caught an exception')
finally:
    print('In finally block for cleanup')
