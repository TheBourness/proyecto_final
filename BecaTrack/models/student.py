from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from models.base import Base

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    student_code = Column(String(50), unique=True, index=True, nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True)
    phone = Column(String(20))
    university = Column(String(150))
    career = Column(String(150))
    current_semester = Column(Integer, default=1)
    
    # Para saber si la beca está activa
    is_active = Column(Boolean, default=True)
    
    # Relaciones
    trackings = relationship("Tracking", back_populates="student", cascade="all, delete-orphan")
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
