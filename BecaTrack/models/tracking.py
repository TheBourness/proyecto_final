from sqlalchemy import Column, Integer, String, Float, Boolean, Date, Text, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base
import datetime

class Tracking(Base):
    __tablename__ = 'trackings'

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, default=datetime.date.today, nullable=False)
    
    # Tipo: Presencial, Llamada, Virtual
    tracking_type = Column(String(50), nullable=False)
    
    # Asistencia y tareas
    attended = Column(Boolean, default=True)
    completed_tasks = Column(Boolean, default=True)
    
    # Métricas
    volunteer_hours = Column(Float, default=0.0)
    academic_grade = Column(Float, default=0.0)
    
    # Estado académico: Excelente, Regular, En Riesgo
    academic_status = Column(String(50), default="Regular")
    
    # Comentarios
    comments = Column(Text)
    
    # Claves foráneas
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    monitor_id = Column(Integer, ForeignKey("monitors.id"), nullable=True)
    
    # Relaciones
    student = relationship("Student", back_populates="trackings")
    monitor = relationship("Monitor", back_populates="trackings")
