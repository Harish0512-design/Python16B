# Define a class named American which has a static method called
# printNationality.
# Hints:
# Use @staticmethod decorator to define class static method.
#
# class American:
#     nationality = "American"
#
#     @staticmethod
#     def print_nationality():
#         print(American.nationality)
#
#
# American.print_nationality()
# american = American()
# american.print_nationality()


class American(object):
    @staticmethod
    def print_nationality():
        print("America")


anAmerican = American()
anAmerican.print_nationality()
American.print_nationality()
