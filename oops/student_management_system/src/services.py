from oops.student_management_system.src.repository import StudentRepository
from oops.student_management_system.src.models import Student
from typing import List, Optional


class StudentService:
    """
    Handles business logic.
    This layer acts as an interface between user and repository.
    """

    def __init__(self):
        self.repo = StudentRepository()

    def create_student(self, name: str, age: int, email: str, grade: str) -> None:
        student = Student(name, age, email, grade)
        self.repo.add_student(student)

    def list_students(self) -> List[Student]:
        self.repo.get_all()

    def find_student(self, student_id) -> Optional[Student]:
        self.repo.get_by_id(student_id)

    def update_student(self, student_id) -> bool:
        student = self.find_student(student_id)
        self.repo.update(student)

    def delete_student(self, student_id) -> bool:
        self.repo.delete(student_id)
