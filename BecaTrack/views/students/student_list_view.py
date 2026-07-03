import customtkinter as ctk
from config import COLOR_PALETTE

class StudentListView(ctk.CTkFrame):
    """Vista de listado de estudiantes (CRUD - Read)"""
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="transparent")
        self.controller = controller
        self._setup_ui()
        
    def _setup_ui(self):
        # Header (Buscar y Añadir)
        self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.header_frame.pack(fill="x", pady=(0, 10))
        
        self.search_entry = ctk.CTkEntry(self.header_frame, placeholder_text="Buscar estudiante...", width=300)
        self.search_entry.pack(side="left", padx=(0, 10))
        
        self.search_btn = ctk.CTkButton(self.header_frame, text="Buscar", width=100, command=self.controller.search_students)
        self.search_btn.pack(side="left")
        
        self.add_btn = ctk.CTkButton(
            self.header_frame, text="+ Nuevo Estudiante", fg_color=COLOR_PALETTE["green"], hover_color="#16A34A",
            command=self.controller.show_add_form
        )
        self.add_btn.pack(side="right")
        
        # Tabla (ScrollableFrame)
        self.table_frame = ctk.CTkScrollableFrame(self, fg_color=COLOR_PALETTE["dark_gray"])
        self.table_frame.pack(fill="both", expand=True)
        
        # Encabezados
        headers = ["Código", "Nombre", "Universidad", "Carrera", "Semestre", "Acciones"]
        for col, h in enumerate(headers):
            lbl = ctk.CTkLabel(self.table_frame, text=h, font=ctk.CTkFont(weight="bold"))
            lbl.grid(row=0, column=col, padx=15, pady=10, sticky="w")
            
        self.table_rows = []
        
    def load_students(self, students):
        # Limpiar tabla
        for row in self.table_rows:
            for widget in row:
                widget.destroy()
        self.table_rows.clear()
        
        for i, s in enumerate(students):
            row_idx = i + 1
            
            code = ctk.CTkLabel(self.table_frame, text=s.student_code)
            code.grid(row=row_idx, column=0, padx=15, pady=5, sticky="w")
            
            name = ctk.CTkLabel(self.table_frame, text=s.full_name)
            name.grid(row=row_idx, column=1, padx=15, pady=5, sticky="w")
            
            uni = ctk.CTkLabel(self.table_frame, text=s.university or "N/A")
            uni.grid(row=row_idx, column=2, padx=15, pady=5, sticky="w")
            
            career = ctk.CTkLabel(self.table_frame, text=s.career or "N/A")
            career.grid(row=row_idx, column=3, padx=15, pady=5, sticky="w")
            
            sem = ctk.CTkLabel(self.table_frame, text=str(s.current_semester))
            sem.grid(row=row_idx, column=4, padx=15, pady=5, sticky="w")
            
            action_frame = ctk.CTkFrame(self.table_frame, fg_color="transparent")
            action_frame.grid(row=row_idx, column=5, padx=15, pady=5, sticky="w")
            
            # Placeholder para ver detalle
            view_btn = ctk.CTkButton(action_frame, text="Ver", width=50, height=25, command=lambda sid=s.id: self.controller.view_student(sid))
            view_btn.pack(side="left", padx=2)
            
            self.table_rows.append((code, name, uni, career, sem, action_frame, view_btn))
