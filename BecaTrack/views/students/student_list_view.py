import customtkinter as ctk
from config import COLOR_PALETTE

class StudentListView(ctk.CTkFrame):
    """Vista de listado de estudiantes estilo web moderno."""
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="transparent")
        self.controller = controller
        self._setup_ui()
        
    def _setup_ui(self):
        # Card principal
        self.card = ctk.CTkFrame(self, fg_color=COLOR_PALETTE["bg_card"], corner_radius=15, border_width=1, border_color=COLOR_PALETTE["border"])
        self.card.pack(fill="both", expand=True, padx=30, pady=30)
        
        # Header (Buscar y Añadir)
        self.header_frame = ctk.CTkFrame(self.card, fg_color="transparent")
        self.header_frame.pack(fill="x", padx=30, pady=(30, 20))
        
        # Titulo
        self.title_lbl = ctk.CTkLabel(
            self.header_frame, text="Directorio de Estudiantes", 
            font=ctk.CTkFont(family="Inter", size=18, weight="bold"), 
            text_color=COLOR_PALETTE["text_primary"]
        )
        self.title_lbl.pack(side="left")
        
        # Boton añadir
        self.add_btn = ctk.CTkButton(
            self.header_frame, text="+ Nuevo Estudiante", 
            fg_color=COLOR_PALETTE["blue"], font=ctk.CTkFont(weight="bold"), 
            height=35, corner_radius=8,
            command=self.controller.show_add_form
        )
        self.add_btn.pack(side="right")
        
        # Buscador
        self.search_entry = ctk.CTkEntry(
            self.header_frame, placeholder_text="🔍 Buscar estudiante...", width=250, height=35,
            fg_color=COLOR_PALETTE["bg_app"], border_color=COLOR_PALETTE["border"], border_width=1,
            text_color=COLOR_PALETTE["text_primary"]
        )
        self.search_entry.pack(side="right", padx=15)
        
        self.search_btn = ctk.CTkButton(
            self.header_frame, text="Buscar", width=80, height=35, corner_radius=8, 
            fg_color="transparent", text_color=COLOR_PALETTE["text_primary"], 
            border_width=1, border_color=COLOR_PALETTE["border"], hover_color=COLOR_PALETTE["bg_app"],
            command=self.controller.search_students
        )
        self.search_btn.pack(side="right", padx=(0, 5))
        
        # Separator
        self.separator = ctk.CTkFrame(self.card, height=1, fg_color=COLOR_PALETTE["border"])
        self.separator.pack(fill="x", padx=30)
        
        # Table Headers
        self.table_headers = ctk.CTkFrame(self.card, fg_color="transparent")
        self.table_headers.pack(fill="x", padx=30, pady=10)
        
        headers = ["CÓDIGO", "ESTUDIANTE", "UNIVERSIDAD", "CARRERA", "SEMESTRE", "ACCIÓN"]
        self.weights = [1, 2, 2, 2, 1, 1]
        
        for i, h in enumerate(headers):
            self.table_headers.grid_columnconfigure(i, weight=self.weights[i])
            lbl = ctk.CTkLabel(self.table_headers, text=h, font=ctk.CTkFont(size=11, weight="bold"), text_color=COLOR_PALETTE["text_secondary"])
            lbl.grid(row=0, column=i, sticky="w", padx=10)
            
        # Tabla Content
        self.table_scroll = ctk.CTkScrollableFrame(self.card, fg_color="transparent")
        self.table_scroll.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        self.table_rows = []
        
    def load_students(self, students):
        for row in self.table_rows:
            row.destroy()
        self.table_rows.clear()
        
        for i, w in enumerate(self.weights):
            self.table_scroll.grid_columnconfigure(i, weight=w)
            
        if not students:
            self._render_mock_data()
            return
            
        for row_idx, s in enumerate(students):
            self._create_row(row_idx, s.student_code, s.full_name, s.university, s.career, s.current_semester, s.id)
            
    def _create_row(self, row_idx, code, name, uni, career, sem, s_id):
        row_frame = ctk.CTkFrame(self.table_scroll, fg_color="transparent")
        row_frame.grid(row=row_idx * 2, column=0, columnspan=6, sticky="ew", pady=(10, 0))
        
        for i, w in enumerate(self.weights):
            row_frame.grid_columnconfigure(i, weight=w)
            
        col0 = ctk.CTkFrame(row_frame, fg_color="transparent")
        col0.grid(row=0, column=0, sticky="w", padx=10)
        ctk.CTkLabel(col0, text=code, font=ctk.CTkFont(weight="bold", size=13), text_color=COLOR_PALETTE["text_primary"]).pack(anchor="w")
        
        col1 = ctk.CTkFrame(row_frame, fg_color="transparent")
        col1.grid(row=0, column=1, sticky="w", padx=10)
        ctk.CTkLabel(col1, text=name, font=ctk.CTkFont(weight="bold", size=14), text_color=COLOR_PALETTE["text_primary"]).pack(anchor="w")
        
        col2 = ctk.CTkFrame(row_frame, fg_color="transparent")
        col2.grid(row=0, column=2, sticky="w", padx=10)
        ctk.CTkLabel(col2, text=uni or "N/A", font=ctk.CTkFont(size=13), text_color=COLOR_PALETTE["text_secondary"]).pack(anchor="w")
        
        col3 = ctk.CTkFrame(row_frame, fg_color="transparent")
        col3.grid(row=0, column=3, sticky="w", padx=10)
        ctk.CTkLabel(col3, text=career or "N/A", font=ctk.CTkFont(size=13), text_color=COLOR_PALETTE["text_secondary"]).pack(anchor="w")
        
        col4 = ctk.CTkFrame(row_frame, fg_color="transparent")
        col4.grid(row=0, column=4, sticky="w", padx=10)
        ctk.CTkLabel(col4, text=str(sem), font=ctk.CTkFont(weight="bold", size=13), text_color=COLOR_PALETTE["text_primary"]).pack(anchor="w")
        
        col5 = ctk.CTkFrame(row_frame, fg_color="transparent")
        col5.grid(row=0, column=5, sticky="e", padx=10)
        ctk.CTkButton(
            col5, text="Ver Perfil", fg_color="transparent", text_color=COLOR_PALETTE["blue"], 
            hover_color=COLOR_PALETTE["bg_app"], width=60, font=ctk.CTkFont(weight="bold"),
            command=lambda sid=s_id: self.controller.view_student(sid)
        ).pack(anchor="e")
        
        sep = ctk.CTkFrame(self.table_scroll, height=1, fg_color=COLOR_PALETTE["border"])
        sep.grid(row=row_idx * 2 + 1, column=0, columnspan=6, sticky="ew", pady=(10, 0))
        
        self.table_rows.extend([row_frame, sep])

    def _render_mock_data(self):
        mocks = [
            ("00125", "Sofía Reyes", "Universidad Nacional", "Ing. en Sistemas", 5),
            ("00311", "Mario Castellanos", "Universidad Tecnológica", "Administración", 3),
            ("00084", "Ana Martínez", "Universidad Católica", "Medicina", 1),
            ("00482", "Carlos Pérez", "Instituto Politécnico", "Diseño Gráfico", 2),
            ("00592", "Luis Fernando", "Universidad Nacional", "Arquitectura", 4)
        ]
        for i, (code, name, uni, career, sem) in enumerate(mocks):
            self._create_row(i, code, name, uni, career, sem, i)
