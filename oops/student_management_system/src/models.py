from typing import Optional
from oops.student_management_system.src.entities import BaseEntity


class Student(BaseEntity):
    """
    Concrete implementation of BaseEntity.
    Represents a student.
    """

    def __init__(self, name: str, age: int, email: str, grade: str, student_id: Optional[int] = None):
        self.__id = student_id
        self.__name = name
        self.__age = age
        self.__email = email
        self.__grade = grade

    # Getters
    def get_id(self) -> Optional[int]:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def get_age(self) -> int:
        return self.__age

    def get_email(self) -> str:
        return self.__email

    def get_grade(self) -> str:
        return self.__grade

    # Setters
    def set_id(self, id: int) -> None:
        self.__id = id

    def set_name(self, name: str) -> None:
        self.__name = name

    def set_age(self, age: int) -> None:
        self.__age = age

    def set_email(self, email: str) -> None:
        self.__email = email

    def set_grade(self, grade: str) -> None:
        self.__grade = grade
