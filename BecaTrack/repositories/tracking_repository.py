from sqlalchemy.orm import Session
from models.tracking import Tracking
from typing import List

class TrackingRepository:
    """Repositorio para interactuar con la tabla de seguimientos (trackings)."""
    
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[Tracking]:
        return self.session.query(Tracking).order_by(Tracking.date.desc()).all()

    def get_by_student(self, student_id: int) -> List[Tracking]:
        return self.session.query(Tracking).filter(
            Tracking.student_id == student_id
        ).order_by(Tracking.date.desc()).all()

    def get_latest(self, limit: int = 5) -> List[Tracking]:
        return self.session.query(Tracking).order_by(Tracking.date.desc()).limit(limit).all()

    def create(self, tracking: Tracking) -> Tracking:
        self.session.add(tracking)
        self.session.commit()
        self.session.refresh(tracking)
        return tracking

    def update(self) -> None:
        self.session.commit()
        
    def delete(self, tracking: Tracking) -> None:
        self.session.delete(tracking)
        self.session.commit()
