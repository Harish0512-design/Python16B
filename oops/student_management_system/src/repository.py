from typing import List, Optional
from oops.student_management_system.src.interfaces import IRepository
from oops.student_management_system.src.models import Student
from oops.student_management_system.src.db import get_connection


class StudentRepository(IRepository[Student]):
    """
    Concrete repository for Student entity using SQLITE3.
    Implements the generic IRepository Interface.
    """
    INSERT_QUERY = "INSERT INTO STUDENTS (name, age, email, grade) VALUES (?, ?, ?, ?)"
    SELECT_QUERY = "SELECT * FROM STUDENTS WHERE id = ?"
    SELECT_ALL_QUERY = "SELECT * FROM STUDENTS"
    UPDATE_QUERY = "UPDATE STUDENTS SET name = ?, age = ?, email = ?, grade = ? WHERE id = ?"
    DELETE_QUERY = "DELETE FROM STUDENTS WHERE id = ?"

    def add(self, student: Student) -> None:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(StudentRepository.INSERT_QUERY,
                       (
                           student.get_name(), student.get_age(),
                           student.get_email(), student.get_grade()
                       )
                       )

    def get_by_id(self, student_id: int) -> Optional[Student]:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(StudentRepository.SELECT_QUERY, (student_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Student(row[1], row[2], row[3], row[4], row[0])
        return None

    def get_all(self) -> List[Student]:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(StudentRepository.SELECT_ALL_QUERY)
        rows = cursor.fetchall()
        conn.close()
        return [
            Student(row[1], row[2], row[3], row[4], row[0])
            for row in rows
        ]

    def update(self, student: Student) -> bool:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            StudentRepository.UPDATE_QUERY,
            (student.get_name(), student.get_age(),
             student.get_email(), student.get_grade(), student.get_id())
        )
        conn.commit()
        updated = cursor.rowcount
        conn.close()
        return updated > 0

    def delete(self, student_id: int) -> bool:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            StudentRepository.DELETE_QUERY, (student_id,)
        )
        conn.commit()
        deleted = cursor.rowcount
        conn.close()
        return deleted > 0
