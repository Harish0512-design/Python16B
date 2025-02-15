from datetime import date


class Person:
    def __init__(self):
        print("constructor called.")
        print("Constructor is called automatically when an instance is created.")

# 'self' represents the individual object


p1 = Person()
print(p1)

# output:
# constructor called.
# Constructor is called automatically when an instance is created.
# <__main__.Person object at 0x723b6ebab170>


class Person:
    def __init__(self):
        # instance variables
        self.name = "Harish"
        self.age = 26


p1 = Person()
print(p1)
# access the instance variables
print(p1.name)
print(p1.age)

# output:
# <__main__.Person object at 0x782b32fab3b0>
# Harish
# 26


class Person:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


p1 = Person("Harish", 26, 120000)
# access instance variable
print(p1.name)
print(p1.salary)

# modify the value of a variable
p1.salary = 83000

print(p1.salary)

# output:
# <__main__.Person object at 0x782b32fab3b0>
# Harish
# 26


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        # distructor
        # calls after deletion of object
        print("Object deleted.")

    def __str__(self):
        # instead of printing <__main__.Person object at 0x782b32fab3b0>
        # it will prints a well-structed message
        return "Name: {}, Age: {}".format(self.name, self.age)


p1 = Person("Harish", 26)
print(p1)
del p1


# output:
# Name: Harish, Age: 26
# Object deleted.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_birth_year(self):
        # instance method : method works with data of individual objects
        current_year = date.today().year
        print(current_year)
        birth_year = current_year - self.age
        return birth_year


p1 = Person("Harish", 27)
print(p1.get_birth_year())

# output:
# 2025
# 1998


class Person:
    # class variable or static variable:
    # belongs to class (like global variable)
    # independent from instances
    no_of_objects = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.no_of_objects += 1


p1 = Person("Harish", 27)
p2 = Person("Yaswanth", 23)

# all instances have the same value for class variable
print(p1.no_of_objects)
print(p2.no_of_objects)

# modify the class variable
p1.no_of_objects = 4
print(p1.no_of_objects)
print(p2.no_of_objects)

# output:
# 2
# 2
# 4
# 2
