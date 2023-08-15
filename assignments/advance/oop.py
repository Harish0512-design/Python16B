# Object-oriented Programming:

# 1. simplifies the code maintenance
# 2. modularity for easy troubleshooting
# 3. re-usability through inheritance
# 4. flexibility through polymorphism
# 5. security through abstraction


# class and object
# self is the default variable which is always pointing to current object (like this keyword in Java)
# By using self we can access instance variables and instance methods of object.
# class Person:
#     """ This is a person class contains name, age"""
#
#     # initialization method or constructor
#     def __init__(self):
#         # instance variables
#         self.name = "Ram"
#         self.age = 23
#
#     # instance method
#     def display_details(self):
#         return self.name, self.age
#
#
# # object creation ClassName(), ram is a reference variable
# ram = Person()
# # <__main__.Person object at 0x000001173C705580>
# print(ram)
#
# # or we can also get class documentation by className.__doc__
# # This is a person class contains name, age
# print(ram.__doc__)
#
# # instance variables {'name': 'Ram', 'age': 23}
# print(ram.__dict__)


# OOP principles:

# 1. Encapsulation:
# wrapping up of data and functions into one single unit (i.e., class).
# Keeps data safe by without giving access to other classes

# class Student:
#     __college_name = "SVU"
#
#     def __int__(self, name, age, roll_no):
#         self.__name = name
#         self.__age = age
#         self.__roll_no = roll_no
#
#     @staticmethod
#     def get_college_name():
#         return Student.__college_name
#
#     @staticmethod
#     def set_college_name(college_name):
#         Student.__college_name = college_name
#
#     def get_name(self):
#         return self.__name
#
#     def set_name(self):
#         pass

class Employee:
    company = 'TTT'

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_email(self):
        return f"{self.first_name}.{self.last_name}@{Employee.company}.com"

    @classmethod
    def change_company(cls, new_name):
        cls.company = new_name

    @staticmethod
    def static_method():
        return Employee.company
        # print("This an static method")


Employee.change_company("TweakTalent")
emp = Employee("John", "Smith")
print(emp.get_email())
print(Employee.static_method())
emp.static_method()
