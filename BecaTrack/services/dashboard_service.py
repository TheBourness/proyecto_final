from repositories.student_repository import StudentRepository
from repositories.tracking_repository import TrackingRepository
from typing import Dict, Any

class DashboardService:
    """Servicio para calcular métricas (KPIs) del dashboard."""
    
    def __init__(self, student_repo: StudentRepository, tracking_repo: TrackingRepository):
        self.student_repo = student_repo
        self.tracking_repo = tracking_repo

    def get_kpis(self) -> Dict[str, Any]:
        students = self.student_repo.get_all()
        trackings = self.tracking_repo.get_all()
        
        total_students = len(students)
        total_trackings = len(trackings)
        
        total_grades = sum(t.academic_grade for t in trackings if t.academic_grade)
        avg_grade = (total_grades / total_trackings) if total_trackings > 0 else 0.0
        
        attended_trackings = sum(1 for t in trackings if t.attended)
        attendance_rate = (attended_trackings / total_trackings * 100) if total_trackings > 0 else 0.0
        
        at_risk = sum(1 for t in trackings if t.academic_status == "En Riesgo")
        volunteer_hours = sum(t.volunteer_hours for t in trackings if t.volunteer_hours)
        
        return {
            "total_students": total_students,
            "total_trackings": total_trackings,
            "avg_grade": round(avg_grade, 2),
            "attendance_rate": round(attendance_rate, 2),
            "at_risk_students": at_risk,
            "total_volunteer_hours": round(volunteer_hours, 2)
        }
        
    def get_recent_trackings(self, limit: int = 5):
        return self.tracking_repo.get_latest(limit)
