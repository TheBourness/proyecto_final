from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from models.student import Student
from config import REPORTS_DIR
import os
from datetime import datetime

class ReportService:
    """Servicio para la generación de reportes (PDF/Excel)."""
    
    def __init__(self):
        pass

    def generate_student_pdf(self, student: Student, trackings: list) -> str:
        filename = f"Reporte_{student.student_code}_{datetime.now().strftime('%Y%m%d%H%M%S')}.pdf"
        filepath = os.path.join(REPORTS_DIR, filename)
        
        c = canvas.Canvas(filepath, pagesize=letter)
        c.setFont("Helvetica-Bold", 16)
        c.drawString(50, 750, f"Reporte de Seguimiento: {student.full_name}")
        
        c.setFont("Helvetica", 12)
        c.drawString(50, 720, f"Código: {student.student_code}")
        c.drawString(50, 700, f"Carrera: {student.career}")
        c.drawString(50, 680, f"Universidad: {student.university}")
        
        y_pos = 640
        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, y_pos, "Historial de Seguimientos")
        y_pos -= 30
        
        c.setFont("Helvetica", 10)
        for t in trackings:
            if y_pos < 50:
                c.showPage()
                c.setFont("Helvetica", 10)
                y_pos = 750
            
            # Formato simple de línea por seguimiento
            text = f"Fecha: {t.date} | Tipo: {t.tracking_type} | Nota: {t.academic_grade} | Voluntariado: {t.volunteer_hours}h | Estado: {t.academic_status}"
            c.drawString(50, y_pos, text)
            y_pos -= 20
            
        c.save()
        return filepath
