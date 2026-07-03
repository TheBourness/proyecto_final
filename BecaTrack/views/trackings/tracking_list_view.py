import customtkinter as ctk
from config import COLOR_PALETTE

class TrackingListView(ctk.CTkFrame):
    """Vista del listado de seguimientos."""
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="transparent")
        self.controller = controller
        self._setup_ui()
        
    def _setup_ui(self):
        self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.header_frame.pack(fill="x", pady=(0, 10))
        
        self.title_lbl = ctk.CTkLabel(self.header_frame, text="Últimos Seguimientos", font=ctk.CTkFont(size=20, weight="bold"))
        self.title_lbl.pack(side="left")
        
        self.add_btn = ctk.CTkButton(
            self.header_frame, text="+ Registrar Seguimiento", fg_color=COLOR_PALETTE["green"], hover_color="#16A34A",
            command=self.controller.show_add_form
        )
        self.add_btn.pack(side="right")
        
        self.table_frame = ctk.CTkScrollableFrame(self, fg_color=COLOR_PALETTE["dark_gray"])
        self.table_frame.pack(fill="both", expand=True)
        
        headers = ["Fecha", "Estudiante", "Tipo", "Nota", "Voluntariado", "Estado", "Acciones"]
        for col, h in enumerate(headers):
            lbl = ctk.CTkLabel(self.table_frame, text=h, font=ctk.CTkFont(weight="bold"))
            lbl.grid(row=0, column=col, padx=15, pady=10, sticky="w")
            
        self.table_rows = []
        
    def load_trackings(self, trackings):
        for row in self.table_rows:
            for widget in row:
                widget.destroy()
        self.table_rows.clear()
        
        for i, t in enumerate(trackings):
            row_idx = i + 1
            
            date = ctk.CTkLabel(self.table_frame, text=str(t.date))
            date.grid(row=row_idx, column=0, padx=15, pady=5, sticky="w")
            
            s_name = t.student.full_name if t.student else "Desconocido"
            name = ctk.CTkLabel(self.table_frame, text=s_name)
            name.grid(row=row_idx, column=1, padx=15, pady=5, sticky="w")
            
            ttype = ctk.CTkLabel(self.table_frame, text=t.tracking_type)
            ttype.grid(row=row_idx, column=2, padx=15, pady=5, sticky="w")
            
            grade = ctk.CTkLabel(self.table_frame, text=str(t.academic_grade))
            grade.grid(row=row_idx, column=3, padx=15, pady=5, sticky="w")
            
            vol = ctk.CTkLabel(self.table_frame, text=f"{t.volunteer_hours}h")
            vol.grid(row=row_idx, column=4, padx=15, pady=5, sticky="w")
            
            status = ctk.CTkLabel(self.table_frame, text=t.academic_status)
            status.grid(row=row_idx, column=5, padx=15, pady=5, sticky="w")
            
            action_frame = ctk.CTkFrame(self.table_frame, fg_color="transparent")
            action_frame.grid(row=row_idx, column=6, padx=15, pady=5, sticky="w")
            
            view_btn = ctk.CTkButton(action_frame, text="Ver", width=50, height=25, command=lambda tid=t.id: self.controller.view_tracking(tid))
            view_btn.pack(side="left", padx=2)
            
            self.table_rows.append((date, name, ttype, grade, vol, status, action_frame, view_btn))
