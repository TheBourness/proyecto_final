from sqlalchemy.orm import Session
from models.monitor import Monitor
from typing import List

class MonitorRepository:
    """Repositorio para interactuar con la tabla de monitores."""
    
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[Monitor]:
        return self.session.query(Monitor).all()

    def get_by_id(self, monitor_id: int) -> Monitor | None:
        return self.session.query(Monitor).filter(Monitor.id == monitor_id).first()

    def create(self, monitor: Monitor) -> Monitor:
        self.session.add(monitor)
        self.session.commit()
        self.session.refresh(monitor)
        return monitor

    def update(self) -> None:
        self.session.commit()
        
    def delete(self, monitor: Monitor) -> None:
        self.session.delete(monitor)
        self.session.commit()
