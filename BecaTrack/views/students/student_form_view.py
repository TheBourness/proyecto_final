import customtkinter as ctk
from config import COLOR_PALETTE

class StudentFormView(ctk.CTkFrame):
    """Formulario para agregar o editar estudiantes (CRUD - Create/Update)"""
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="transparent")
        self.controller = controller
        self._setup_ui()
        
    def _setup_ui(self):
        # Contenedor central (tarjeta)
        self.card = ctk.CTkScrollableFrame(self, fg_color=COLOR_PALETTE["dark_gray"], corner_radius=10, width=500)
        self.card.pack(pady=20, padx=20, fill="both", expand=True)
        
        self.title_lbl = ctk.CTkLabel(self.card, text="Registrar Estudiante", font=ctk.CTkFont(size=20, weight="bold"))
        self.title_lbl.pack(pady=20)
        
        self.fields = {}
        fields_info = [
            ("Código", "student_code"),
            ("Nombre", "first_name"),
            ("Apellido", "last_name"),
            ("Email", "email"),
            ("Teléfono", "phone"),
            ("Universidad", "university"),
            ("Carrera", "career"),
            ("Semestre (Ej. 1,2,3)", "current_semester")
        ]
        
        for label_text, key in fields_info:
            frame = ctk.CTkFrame(self.card, fg_color="transparent")
            frame.pack(fill="x", padx=40, pady=10)
            
            lbl = ctk.CTkLabel(frame, text=label_text, width=150, anchor="w")
            lbl.pack(side="left")
            
            entry = ctk.CTkEntry(frame, width=300)
            entry.pack(side="right", fill="x", expand=True)
            self.fields[key] = entry
            
        # Botones
        self.btn_frame = ctk.CTkFrame(self.card, fg_color="transparent")
        self.btn_frame.pack(pady=30)
        
        self.cancel_btn = ctk.CTkButton(
            self.btn_frame, text="Cancelar", fg_color=COLOR_PALETTE["red"], hover_color="#B91C1C", command=self.controller.show_list
        )
        self.cancel_btn.pack(side="left", padx=10)
        
        self.save_btn = ctk.CTkButton(
            self.btn_frame, text="Guardar", fg_color=COLOR_PALETTE["blue"], hover_color="#1D4ED8", command=self.controller.save_student
        )
        self.save_btn.pack(side="right", padx=10)
        
        self.msg_lbl = ctk.CTkLabel(self.card, text="", text_color=COLOR_PALETTE["green"])
        self.msg_lbl.pack(pady=5)
        
    def get_data(self):
        data = {}
        for k, entry in self.fields.items():
            val = entry.get()
            if k == "current_semester":
                val = int(val) if val.isdigit() else 1
            data[k] = val
        return data
        
    def clear(self):
        for entry in self.fields.values():
            entry.delete(0, "end")
        self.msg_lbl.configure(text="")
