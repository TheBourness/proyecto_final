from views.trackings.tracking_list_view import TrackingListView
from views.trackings.tracking_form_view import TrackingFormView
from repositories.tracking_repository import TrackingRepository
from repositories.student_repository import StudentRepository
from models.tracking import Tracking

class TrackingController:
    """Controlador real para el módulo de Seguimientos."""
    def __init__(self, parent_frame, tracking_repo: TrackingRepository, student_repo: StudentRepository):
        self.parent_frame = parent_frame
        self.tracking_repo = tracking_repo
        self.student_repo = student_repo
        
        self.list_view = TrackingListView(parent_frame, self)
        self.form_view = TrackingFormView(parent_frame, self)
        
    def get_view(self):
        return self
        
    def pack(self, **kwargs):
        self.show_list()
        
    def pack_forget(self):
        self.list_view.pack_forget()
        self.form_view.pack_forget()

    def show_list(self):
        self.form_view.pack_forget()
        self.list_view.pack(fill="both", expand=True)
        self._refresh_list()
        
    def show_add_form(self):
        self.list_view.pack_forget()
        self.form_view.clear()
        self.form_view.pack(fill="both", expand=True)
        
    def save_tracking(self):
        data = self.form_view.get_data()
        
        if data["student_id"] <= 0:
            self.form_view.msg_lbl.configure(text="Error: ID de Estudiante inválido (debe ser numérico)", text_color="red")
            return
            
        student = self.student_repo.get_by_id(data["student_id"])
        if not student:
            self.form_view.msg_lbl.configure(text="Error: No existe ningún estudiante con ese ID", text_color="red")
            return
            
        try:
            tracking = Tracking(**data)
            self.tracking_repo.create(tracking)
            self.form_view.msg_lbl.configure(text="Seguimiento guardado con éxito", text_color="green")
            self.show_list()
        except Exception as e:
            self.form_view.msg_lbl.configure(text=f"Error al guardar: {e}", text_color="red")
            
    def _refresh_list(self):
        trackings = self.tracking_repo.get_all()
        self.list_view.load_trackings(trackings)
        
    def view_tracking(self, tracking_id):
        print(f"Abriendo detalle del seguimiento {tracking_id}")
