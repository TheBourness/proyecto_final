from views.app_view import AppView
from views.dashboard_view import DashboardView
from services.dashboard_service import DashboardService
from services.student_service import StudentService
from repositories.student_repository import StudentRepository
from repositories.tracking_repository import TrackingRepository
from controllers.student_controller import StudentController
from controllers.tracking_controller import TrackingController

class MainController:
    """Controlador central que gestiona la navegación de la aplicación principal."""
    
    def __init__(self, view: AppView, session):
        self.view = view
        self.session = session
        
        # Inicializar Servicios para las vistas
        self.student_repo = StudentRepository(self.session)
        self.tracking_repo = TrackingRepository(self.session)
        self.student_service = StudentService(self.student_repo)
        self.dashboard_service = DashboardService(self.student_repo, self.tracking_repo)
        
        # Inicializar vistas hijas
        self._setup_views()

    def _setup_views(self):
        # 1. Instanciar Dashboard
        dashboard_view = DashboardView(self.view.content_frame, self.dashboard_service)
        self.view.frames["Dashboard"] = dashboard_view
        
        # 2. Instanciar Módulo Estudiantes
        student_ctrl = StudentController(self.view.content_frame, self.student_service)
        self.view.frames["Directorio Becados"] = student_ctrl
        
        # 3. Instanciar Módulo Seguimientos
        tracking_ctrl = TrackingController(self.view.content_frame, self.tracking_repo, self.student_repo)
        self.view.frames["Control de Seguimientos"] = tracking_ctrl
        
        # Frames temporales para el resto
        import customtkinter as ctk
        sections = ["Métricas y Reportes", "Configuración"]
        
        for sec in sections:
            frame = ctk.CTkFrame(self.view.content_frame, fg_color="transparent")
            lbl = ctk.CTkLabel(frame, text=f"Pantalla de {sec} (Próximamente)", font=ctk.CTkFont(size=24))
            lbl.pack(expand=True)
            self.view.frames[sec] = frame
            
        # Mostrar Dashboard por defecto
        self.view.show_frame("Dashboard")
