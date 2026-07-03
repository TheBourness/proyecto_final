from views.students.student_list_view import StudentListView
from views.students.student_form_view import StudentFormView
from services.student_service import StudentService

class StudentController:
    """Controlador para el módulo de Estudiantes (Lógica e integración UI)."""
    def __init__(self, parent_frame, student_service: StudentService):
        self.parent_frame = parent_frame
        self.service = student_service
        
        # Inicializar sub-vistas
        self.list_view = StudentListView(parent_frame, self)
        self.form_view = StudentFormView(parent_frame, self)
        
        # Mostrar listado por defecto
        self.show_list()
        
    def get_view(self):
        # Método auxiliar para retornar el contenedor actual, en este caso retornamos el list_view
        # pero es mejor devolver el contenedor principal o exponer pack/unpack.
        # Por simplicidad, el controller maneja el empaquetado directamente en el parent_frame
        return self
        
    def pack(self, **kwargs):
        self.show_list() # Asegura que la lista se muestre al inicializar el módulo
        
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
        
    def save_student(self):
        data = self.form_view.get_data()
        
        if not data.get("student_code") or not data.get("first_name"):
            self.form_view.msg_lbl.configure(text="Error: Código y Nombre son obligatorios", text_color="red")
            return
            
        try:
            self.service.add_student(data)
            self.form_view.msg_lbl.configure(text="Guardado exitosamente", text_color="green")
            self.show_list()
        except Exception as e:
            self.form_view.msg_lbl.configure(text="Error al guardar. El código o email puede estar duplicado.", text_color="red")
            
    def _refresh_list(self):
        students = self.service.get_all_students()
        self.list_view.load_students(students)
        
    def search_students(self):
        query = self.list_view.search_entry.get()
        if not query.strip():
            self._refresh_list()
            return
            
        students = self.service.search_students(query)
        self.list_view.load_students(students)
        
    def view_student(self, student_id):
        print(f"Abriendo detalle del estudiante ID: {student_id}")
        # Lógica para abrir perfil detallado
