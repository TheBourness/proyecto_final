import customtkinter as ctk
from config import COLOR_PALETTE

class TrackingFormView(ctk.CTkFrame):
    """Formulario para agregar seguimientos a un estudiante."""
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="transparent")
        self.controller = controller
        self._setup_ui()
        
    def _setup_ui(self):
        self.card = ctk.CTkScrollableFrame(self, fg_color=COLOR_PALETTE["dark_gray"], corner_radius=10, width=600)
        self.card.pack(pady=20, padx=20, fill="both", expand=True)
        
        self.title_lbl = ctk.CTkLabel(self.card, text="Registrar Seguimiento", font=ctk.CTkFont(size=20, weight="bold"))
        self.title_lbl.pack(pady=20)
        
        self.fields = {}
        
        # ID Estudiante
        frame_student = ctk.CTkFrame(self.card, fg_color="transparent")
        frame_student.pack(fill="x", padx=40, pady=10)
        lbl_s = ctk.CTkLabel(frame_student, text="ID Estudiante", width=150, anchor="w")
        lbl_s.pack(side="left")
        self.student_id_entry = ctk.CTkEntry(frame_student, width=300, placeholder_text="Ej: 1")
        self.student_id_entry.pack(side="right", fill="x", expand=True)
        
        # Tipo
        frame_type = ctk.CTkFrame(self.card, fg_color="transparent")
        frame_type.pack(fill="x", padx=40, pady=10)
        lbl_t = ctk.CTkLabel(frame_type, text="Tipo de Seguimiento", width=150, anchor="w")
        lbl_t.pack(side="left")
        self.type_combo = ctk.CTkComboBox(frame_type, values=["Presencial", "Llamada", "Virtual"], width=300)
        self.type_combo.pack(side="right", fill="x", expand=True)
        
        # Checkboxes (Asistencia y Tareas)
        frame_bool = ctk.CTkFrame(self.card, fg_color="transparent")
        frame_bool.pack(fill="x", padx=40, pady=10)
        self.attended_chk = ctk.CTkCheckBox(frame_bool, text="Asistió a tutoría")
        self.attended_chk.pack(side="left", padx=20)
        self.tasks_chk = ctk.CTkCheckBox(frame_bool, text="Cumplió Tareas")
        self.tasks_chk.pack(side="left", padx=20)
        
        # Valores numéricos
        num_fields = [
            ("Horas Voluntariado", "volunteer_hours"),
            ("Nota Académica", "academic_grade")
        ]
        for label_text, key in num_fields:
            frame = ctk.CTkFrame(self.card, fg_color="transparent")
            frame.pack(fill="x", padx=40, pady=10)
            lbl = ctk.CTkLabel(frame, text=label_text, width=150, anchor="w")
            lbl.pack(side="left")
            entry = ctk.CTkEntry(frame, width=300, placeholder_text="0.0")
            entry.pack(side="right", fill="x", expand=True)
            self.fields[key] = entry
            
        # Estado Académico
        frame_status = ctk.CTkFrame(self.card, fg_color="transparent")
        frame_status.pack(fill="x", padx=40, pady=10)
        lbl_st = ctk.CTkLabel(frame_status, text="Estado Académico", width=150, anchor="w")
        lbl_st.pack(side="left")
        self.status_combo = ctk.CTkComboBox(frame_status, values=["Excelente", "Regular", "En Riesgo"], width=300)
        self.status_combo.pack(side="right", fill="x", expand=True)
        
        # Comentarios
        frame_com = ctk.CTkFrame(self.card, fg_color="transparent")
        frame_com.pack(fill="x", padx=40, pady=10)
        lbl_c = ctk.CTkLabel(frame_com, text="Comentarios", width=150, anchor="nw")
        lbl_c.pack(side="left")
        self.comments_text = ctk.CTkTextbox(frame_com, width=300, height=80)
        self.comments_text.pack(side="right", fill="x", expand=True)
        
        # Controles
        self.btn_frame = ctk.CTkFrame(self.card, fg_color="transparent")
        self.btn_frame.pack(pady=30)
        
        self.cancel_btn = ctk.CTkButton(self.btn_frame, text="Cancelar", fg_color=COLOR_PALETTE["red"], command=self.controller.show_list)
        self.cancel_btn.pack(side="left", padx=10)
        
        self.save_btn = ctk.CTkButton(self.btn_frame, text="Guardar", fg_color=COLOR_PALETTE["blue"], command=self.controller.save_tracking)
        self.save_btn.pack(side="right", padx=10)
        
        self.msg_lbl = ctk.CTkLabel(self.card, text="")
        self.msg_lbl.pack(pady=5)
        
    def get_data(self):
        try:
            student_id = int(self.student_id_entry.get())
        except ValueError:
            student_id = 0
            
        try:
            vol = float(self.fields["volunteer_hours"].get() or 0)
            grade = float(self.fields["academic_grade"].get() or 0)
        except ValueError:
            vol = 0.0
            grade = 0.0
            
        return {
            "student_id": student_id,
            "tracking_type": self.type_combo.get(),
            "attended": bool(self.attended_chk.get()),
            "completed_tasks": bool(self.tasks_chk.get()),
            "volunteer_hours": vol,
            "academic_grade": grade,
            "academic_status": self.status_combo.get(),
            "comments": self.comments_text.get("0.0", "end").strip()
        }
        
    def clear(self):
        self.student_id_entry.delete(0, "end")
        for entry in self.fields.values():
            entry.delete(0, "end")
        self.comments_text.delete("0.0", "end")
        self.msg_lbl.configure(text="")
