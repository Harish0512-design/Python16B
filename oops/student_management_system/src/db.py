import sqlite3
from sqlite3 import Connection

STUDENTS_TABLE_CREATION_QUERY = """
CREATE TABLE IF NOT EXISTS students (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       name TEXT NOT NULL,
       age INTEGER NOT NULL,
       email TEXT UNIQUE NOT NULL,
       grade TEXT NOT NULL            
    )
"""

def get_connection(db_name: str = "students.db") -> Connection:
    """
    Create and return a connection to the SQLite3 database
    """
    return sqlite3.connect(db_name)


def initialize_database():
    """
    Initialize the database with a 'students' table.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(STUDENTS_TABLE_CREATION_QUERY)
    conn.commit()
    conn.close()
