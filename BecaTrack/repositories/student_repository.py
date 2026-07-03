from sqlalchemy.orm import Session
from models.student import Student
from typing import List

class StudentRepository:
    """Repositorio para interactuar con la tabla de estudiantes."""
    
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[Student]:
        return self.session.query(Student).all()

    def get_by_id(self, student_id: int) -> Student | None:
        return self.session.query(Student).filter(Student.id == student_id).first()
        
    def get_by_code(self, student_code: str) -> Student | None:
        return self.session.query(Student).filter(Student.student_code == student_code).first()

    def search(self, query: str) -> List[Student]:
        search_term = f"%{query}%"
        return self.session.query(Student).filter(
            (Student.first_name.ilike(search_term)) |
            (Student.last_name.ilike(search_term)) |
            (Student.student_code.ilike(search_term))
        ).all()

    def create(self, student: Student) -> Student:
        self.session.add(student)
        self.session.commit()
        self.session.refresh(student)
        return student

    def update(self) -> None:
        self.session.commit()

    def delete(self, student: Student) -> None:
        self.session.delete(student)
        self.session.commit()
