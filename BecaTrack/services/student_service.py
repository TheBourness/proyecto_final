from repositories.student_repository import StudentRepository
from models.student import Student
from typing import List

class StudentService:
    """Servicio con la lógica de negocio relacionada a los estudiantes."""
    
    def __init__(self, student_repo: StudentRepository):
        self.student_repo = student_repo

    def get_all_students(self) -> List[Student]:
        return self.student_repo.get_all()

    def add_student(self, data: dict) -> Student:
        student = Student(**data)
        return self.student_repo.create(student)
        
    def update_student(self, student_id: int, data: dict) -> Student | None:
        student = self.student_repo.get_by_id(student_id)
        if student:
            for key, value in data.items():
                setattr(student, key, value)
            self.student_repo.update()
        return student

    def search_students(self, query: str) -> List[Student]:
        return self.student_repo.search(query)
