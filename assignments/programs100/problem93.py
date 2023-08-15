# Define a class Person and its two child classes: Male and Female. All
# classes have a method "getGender" which can print "Male" for Male
# class and "Female" for Female class.
# Hints:
# Use Subclass(Parentclass) to define a child class.

#
# class Person:
#     def get_gender(self):
#         print("Don't know")
#
#
# class Male(Person):
#     def get_gender(self):
#         print("Male")
#
#
# class Female(Person):
#     def get_gender(self):
#         print("Female")


class Person:
    def get_gender(self):
        return 'Unknown'


class Male(Person):
    def get_gender(self):
        return "Male"


class Female(Person):
    def get_gender(self):
        return "Female"


male = Male()
print(male.get_gender())

female = Female()
print(female.get_gender())
