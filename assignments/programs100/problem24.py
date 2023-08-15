# Python
# has
# many
# built - in functions, and if you do not know how to
# use
# it, you
# can
# read
# document
# online or find
# some
# books.But
# Python
# has
# a
# built - in document
# function
# for every built - in functions.
#     Please
#     write
#     a
#     program
#     to
#     print
#     some
#     Python
#     built - in functions
# documents, such as abs(), int(), raw_input()
# And
# add
# document
# for your own function
#
# Hints:
# The
# built - in document
# method is __doc__


print(abs.__doc__)
print('-' * 30)
print(int.__doc__)
print('-' * 30)
print(float.__doc__)
print('-' * 30)
print(input.__doc__)


def calculate_area_of_rectangle(length, breadth):
    ''' Calculates area of the rectangle
        input length: int and breadth: int
        returns area: int
    '''

    return length * breadth


print(calculate_area_of_rectangle(3, 6))
print(calculate_area_of_rectangle.__doc__)

