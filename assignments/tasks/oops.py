# class Employee:
#     def __init__(self):
#         print("Constructor called..")
#         self.__empid = None
#         self.__doj = None
#         self.__salary = None
#
#     def set_empId(self, empId):
#         self.__empid = empId
#
#     def set_doj(self, doj):
#         self.__doj = doj
#
#     def set_salary(self, salary):
#         self.__salary = salary
#
#     def get_empid(self):
#         return self.__empid
#
#     def get_doj(self):
#         return self.__doj
#
#     def get_salary(self):
#         return self.__salary
#
#
# reference_variable = Employee()
#
# # reference_variable.set_doj("12/12/2022")
# # reference_variable.set_empId('E1101')
# # reference_variable.set_salary(45000)
# #
# # print(reference_variable.get_doj())
# # print(reference_variable.get_empid())
# # print(reference_variable.get_salary())


class Student:
    def __init__(self, student_id, marks, age):
        self.__student_id = student_id
        self.__marks = marks
        self.__age = age

    def set_student_id(self, student_id):
        self.__student_id = student_id

    def set_marks(self, marks):
        self.__marks = marks

    def set_age(self, age):
        self.__age = age

    def get_student_id(self):
        return self.__student_id

    def get_marks(self):
        return self.__marks

    def get_age(self):
        return self.__age

    def validate_age(self):
        if self.__age > 20:
            return True
        else:
            return False

    def validate_marks(self):
        if self.__marks >= 0 and self.__marks <= 100:
            return True
        else:
            return False

    def check_qualification(self):
        age_validation = self.validate_age()
        marks_validation = self.validate_marks()
        if age_validation and marks_validation:
            if self.__marks >= 65:
                return True
            else:
                return False
        else:
            return False



# chaitanya = Student(101, 65, 23)
# print(chaitanya.check_qualification())
# chaitanya1 = Student(102, 70, 21)
# print(chaitanya1.check_qualification())
# chaitanya2 = Student(103, 45, 21)
# print(chaitanya2.check_qualification())
# chaitanya3 = Student(104, 90, 19)
# print(chaitanya3.check_qualification())