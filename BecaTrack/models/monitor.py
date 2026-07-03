from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base

class Monitor(Base):
    __tablename__ = 'monitors'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, index=True)
    phone = Column(String(20))
    
    # Relaciones
    trackings = relationship("Tracking", back_populates="monitor")
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
