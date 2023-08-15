# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
# Hints:
# Use __init__ method to construct some parameters

class Sample:
    def __init__(self):
        self.name = None

    def get_string(self):
        self.name = input()

    def print_string(self):
        print(self.name.upper())

    def test(self):
        self.get_string()
        self.print_string()


res_obj = Sample()
res_obj.test()
