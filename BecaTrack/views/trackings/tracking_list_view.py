import customtkinter as ctk
from config import COLOR_PALETTE

class TrackingListView(ctk.CTkFrame):
    """Vista de listado de seguimientos (Historial de Contactos) estilo web moderno."""
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="transparent")
        self.controller = controller
        self._setup_ui()
        
    def _setup_ui(self):
        self.card = ctk.CTkFrame(self, fg_color=COLOR_PALETTE["bg_card"], corner_radius=15, border_width=1, border_color=COLOR_PALETTE["border"])
        self.card.pack(fill="both", expand=True, padx=30, pady=30)
        
        # Header
        self.header = ctk.CTkFrame(self.card, fg_color="transparent")
        self.header.pack(fill="x", padx=30, pady=(30, 20))
        
        self.title_lbl = ctk.CTkLabel(
            self.header, text="Historial Completo de Contactos", 
            font=ctk.CTkFont(family="Inter", size=18, weight="bold"), 
            text_color=COLOR_PALETTE["text_primary"]
        )
        self.title_lbl.pack(side="left")
        
        self.add_btn = ctk.CTkButton(
            self.header, text="+ Nuevo Seguimiento", 
            fg_color=COLOR_PALETTE["blue"], font=ctk.CTkFont(weight="bold"), 
            height=35, corner_radius=8,
            command=self.controller.show_add_form
        )
        self.add_btn.pack(side="right")
        
        # Separator
        self.separator = ctk.CTkFrame(self.card, height=1, fg_color=COLOR_PALETTE["border"])
        self.separator.pack(fill="x", padx=30)
        
        # Table Headers
        self.table_headers = ctk.CTkFrame(self.card, fg_color="transparent")
        self.table_headers.pack(fill="x", padx=30, pady=10)
        
        headers = ["ESTUDIANTE / ID", "FECHA / VÍA", "ASISTENCIA", "TAREAS", "ESTADO / NOTAS", "ACCIÓN"]
        self.weights = [2, 1, 1, 1, 3, 1]
        
        for i, h in enumerate(headers):
            self.table_headers.grid_columnconfigure(i, weight=self.weights[i])
            lbl = ctk.CTkLabel(self.table_headers, text=h, font=ctk.CTkFont(size=11, weight="bold"), text_color=COLOR_PALETTE["text_secondary"])
            lbl.grid(row=0, column=i, sticky="w", padx=10)
            
        # Table Content
        self.table_scroll = ctk.CTkScrollableFrame(self.card, fg_color="transparent")
        self.table_scroll.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        self.table_rows = []
        
    def load_trackings(self, trackings):
        for row in self.table_rows:
            row.destroy()
        self.table_rows.clear()
        
        for i, w in enumerate(self.weights):
            self.table_scroll.grid_columnconfigure(i, weight=w)
            
        # Si no hay registros (base de datos vacía), mostramos unos falsos para previsualizar el diseño
        if not trackings:
            self._render_mock_data()
            return
            
        for row_idx, t in enumerate(trackings):
            s_name = t.student.full_name if t.student else "Desconocido"
            s_id = t.student.student_code if t.student else "000"
            date_str = str(t.date)
            self._create_row(row_idx, s_name, s_id, date_str, t.tracking_type, t.attended, t.completed_tasks, t.academic_status, t.comments, t.id)
            
    def _create_row(self, row_idx, s_name, s_id, date_str, via, attended, tasks, status, comments, t_id):
        row_frame = ctk.CTkFrame(self.table_scroll, fg_color="transparent")
        row_frame.grid(row=row_idx * 2, column=0, columnspan=6, sticky="ew", pady=(10, 0))
        
        for i, w in enumerate(self.weights):
            row_frame.grid_columnconfigure(i, weight=w)
            
        # 1. Estudiante / ID
        col1 = ctk.CTkFrame(row_frame, fg_color="transparent")
        col1.grid(row=0, column=0, sticky="w", padx=10)
        ctk.CTkLabel(col1, text=s_name, font=ctk.CTkFont(weight="bold", size=14), text_color=COLOR_PALETTE["text_primary"]).pack(anchor="w")
        ctk.CTkLabel(col1, text=f"ID: {s_id}", font=ctk.CTkFont(size=12), text_color=COLOR_PALETTE["text_secondary"]).pack(anchor="w")
        
        # 2. Fecha / Vía
        col2 = ctk.CTkFrame(row_frame, fg_color="transparent")
        col2.grid(row=0, column=1, sticky="w", padx=10)
        ctk.CTkLabel(col2, text=date_str, font=ctk.CTkFont(weight="bold", size=13), text_color=COLOR_PALETTE["text_primary"]).pack(anchor="w")
        via_icon = "📞" if "llamada" in str(via).lower() else "📍"
        ctk.CTkLabel(col2, text=f"{via_icon} {via}", font=ctk.CTkFont(size=12), text_color=COLOR_PALETTE["text_secondary"]).pack(anchor="w")
        
        # 3. Asistencia
        col3 = ctk.CTkFrame(row_frame, fg_color="transparent")
        col3.grid(row=0, column=2, sticky="w", padx=10)
        att_txt, att_col = ("✅", COLOR_PALETTE["green"]) if attended else ("⚠️", COLOR_PALETTE["red"])
        ctk.CTkLabel(col3, text=att_txt, text_color=att_col, font=ctk.CTkFont(size=18)).pack(anchor="w", pady=(5,0))
        
        # 4. Tareas
        col4 = ctk.CTkFrame(row_frame, fg_color="transparent")
        col4.grid(row=0, column=3, sticky="w", padx=10)
        tsk_txt, tsk_col = ("✅", COLOR_PALETTE["green"]) if tasks else ("⚠️", COLOR_PALETTE["red"])
        ctk.CTkLabel(col4, text=tsk_txt, text_color=tsk_col, font=ctk.CTkFont(size=18)).pack(anchor="w", pady=(5,0))
        
        # 5. Estado / Notas
        col5 = ctk.CTkFrame(row_frame, fg_color="transparent")
        col5.grid(row=0, column=4, sticky="w", padx=10)
        
        status_map = {
            "Excelente": ("AL DÍA", COLOR_PALETTE["green"], COLOR_PALETTE["green_light"]),
            "Regular": ("OBSERVACIÓN", "#D97706", "#FEF3C7"),
            "En Riesgo": ("ALERTA", COLOR_PALETTE["red"], COLOR_PALETTE["red_light"])
        }
        s_text, s_fg, s_bg = status_map.get(status, ("CRÍTICO", COLOR_PALETTE["red"], COLOR_PALETTE["red_light"]))
        
        tag = ctk.CTkLabel(col5, text=f"  {s_text}  ", text_color=s_fg, fg_color=s_bg, font=ctk.CTkFont(weight="bold", size=10), corner_radius=6)
        tag.pack(anchor="w", pady=(0, 2))
        
        nota = comments if comments else "Sin comentarios."
        if len(nota) > 40: nota = nota[:37] + "..."
        ctk.CTkLabel(col5, text=nota, text_color=COLOR_PALETTE["text_secondary"], font=ctk.CTkFont(size=12)).pack(anchor="w")
        
        # 6. Acción
        col6 = ctk.CTkFrame(row_frame, fg_color="transparent")
        col6.grid(row=0, column=5, sticky="e", padx=10)
        ctk.CTkButton(
            col6, text="Editar", fg_color="transparent", text_color=COLOR_PALETTE["blue"], 
            hover_color=COLOR_PALETTE["bg_app"], width=60, font=ctk.CTkFont(weight="bold"),
            command=lambda tid=t_id: self.controller.view_tracking(tid)
        ).pack(anchor="e", pady=(10,0))
        
        # Divider Line
        sep = ctk.CTkFrame(self.table_scroll, height=1, fg_color=COLOR_PALETTE["border"])
        sep.grid(row=row_idx * 2 + 1, column=0, columnspan=6, sticky="ew", pady=(10, 0))
        
        self.table_rows.extend([row_frame, sep])

    def _render_mock_data(self):
        # Para que se vea igual a la imagen si no hay registros
        mocks = [
            ("Sofía Reyes", "00125", "02 Jul", "Llamada", True, True, "Excelente", "Todo en orden. Voluntariado OK."),
            ("Mario Castellanos", "00311", "01 Jul", "Presencial", False, True, "En Riesgo", "Problemas familiares, faltó 3 días."),
            ("Ana Martínez", "00084", "30 Jun", "Llamada", True, False, "Regular", "Debe tarea de Matemáticas."),
            ("Carlos Pérez", "00482", "28 Jun", "Llamada", True, True, "Excelente", "Listo para los parciales."),
            ("Luis Fernando", "00592", "25 Jun", "Presencial", False, False, "Otros", "No se presentó al taller. Posible ab...")
        ]
        for i, (name, sid, d, via, att, tsk, st, obs) in enumerate(mocks):
            self._create_row(i, name, sid, d, via, att, tsk, st, obs, i)
