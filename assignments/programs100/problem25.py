# Define a class, which have a class parameter and have a same instance parameter.
# Hints:
#  Define a instance parameter, need add it in __init__ method
#  You can init a object with construct parameter or set the value later
class Student:
    st_name = "Student"

    def __init__(self, name=None):
        self.st_name = name

    def get_details(self):
        return "%s name is %s" % (Student.st_name, self.st_name)


s1 = Student("John")
print(s1.get_details())
s2 = Student()
s2.st_name = "Noel"
print(s2.get_details())
