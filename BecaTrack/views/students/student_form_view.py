import customtkinter as ctk
from config import COLOR_PALETTE

class StudentFormView(ctk.CTkFrame):
    """Formulario para agregar estudiantes (estilo web moderno en 2 columnas)."""
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="transparent")
        self.controller = controller
        self._setup_ui()
        
    def _setup_ui(self):
        # Card principal blanca
        self.card = ctk.CTkFrame(self, fg_color=COLOR_PALETTE["bg_card"], corner_radius=15, border_width=1, border_color=COLOR_PALETTE["border"])
        self.card.pack(pady=15, padx=20, fill="both", expand=True)
        
        # Header de la card
        self.header_frame = ctk.CTkFrame(self.card, fg_color="transparent")
        self.header_frame.pack(fill="x", padx=30, pady=(15, 10))
        
        self.title_lbl = ctk.CTkLabel(
            self.header_frame, text="Registrar Nuevo Estudiante", 
            font=ctk.CTkFont(family="Inter", size=20, weight="bold"), 
            text_color=COLOR_PALETTE["text_primary"]
        )
        self.title_lbl.pack(side="left")
        
        self.back_btn = ctk.CTkButton(
            self.header_frame, text="Volver al listado", 
            fg_color="transparent", text_color=COLOR_PALETTE["text_secondary"], 
            hover_color=COLOR_PALETTE["bg_app"], 
            command=self.controller.show_list
        )
        self.back_btn.pack(side="right")
        
        # Separador
        self.separator = ctk.CTkFrame(self.card, height=1, fg_color=COLOR_PALETTE["border"])
        self.separator.pack(fill="x", padx=30, pady=(0, 10))
        
        # Form Container (Grid 2 columnas)
        self.form_container = ctk.CTkFrame(self.card, fg_color="transparent")
        self.form_container.pack(fill="both", expand=True, padx=30)
        self.form_container.grid_columnconfigure((0, 1), weight=1)
        
        self.fields = {}
        
        # Fila 0
        self._create_input(0, 0, "Código", "Ej. 00892", "student_code")
        self._create_input(0, 1, "Semestre / Año", "Ej. 1, 2, 3 o 3er Año", "current_semester")
        
        # Fila 1
        self._create_input(1, 0, "Nombre", "", "first_name")
        self._create_input(1, 1, "Apellido", "", "last_name")
        
        # Fila 2
        self._create_input(2, 0, "Email", "", "email")
        self._create_input(2, 1, "Teléfono", "", "phone")
        
        # Fila 3 y 4 (Ancho completo)
        self._create_input(3, 0, "Universidad", "", "university", colspan=2)
        self._create_input(4, 0, "Carrera", "", "career", colspan=2)
        
        # Footer con botones
        self.footer = ctk.CTkFrame(self.card, fg_color="transparent")
        self.footer.pack(fill="x", padx=40, pady=15)
        
        self.msg_lbl = ctk.CTkLabel(self.footer, text="", font=ctk.CTkFont(size=13, weight="bold"))
        self.msg_lbl.pack(side="left")
        
        self.save_btn = ctk.CTkButton(
            self.footer, text="Guardar Estudiante", 
            fg_color=COLOR_PALETTE["blue"], hover_color="#1D4ED8",
            height=40, corner_radius=8, font=ctk.CTkFont(weight="bold"),
            command=self.controller.save_student
        )
        self.save_btn.pack(side="right")
        
        self.cancel_btn = ctk.CTkButton(
            self.footer, text="Cancelar", 
            fg_color="transparent", text_color=COLOR_PALETTE["text_secondary"], 
            border_width=1, border_color=COLOR_PALETTE["border"], hover_color=COLOR_PALETTE["bg_app"],
            height=40, corner_radius=8, font=ctk.CTkFont(weight="bold"),
            command=self.controller.show_list
        )
        self.cancel_btn.pack(side="right", padx=15)
        
    def _create_input(self, row, col, label_text, placeholder, key, colspan=1):
        frame = ctk.CTkFrame(self.form_container, fg_color="transparent")
        frame.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=10, pady=5)
        
        lbl = ctk.CTkLabel(frame, text=label_text, font=ctk.CTkFont(size=13, weight="bold"), text_color=COLOR_PALETTE["text_secondary"])
        lbl.pack(anchor="w", pady=(0, 2))
        
        entry = ctk.CTkEntry(
            frame, 
            placeholder_text=placeholder, 
            height=35, 
            corner_radius=8,
            fg_color=COLOR_PALETTE["bg_app"], 
            border_color=COLOR_PALETTE["border"],
            border_width=1,
            text_color=COLOR_PALETTE["text_primary"]
        )
        entry.pack(fill="x", expand=True)
        self.fields[key] = entry

    def get_data(self):
        data = {}
        for k, entry in self.fields.items():
            val = entry.get()
            if k == "current_semester":
                val = int(val) if str(val).isdigit() else 1
            data[k] = val
        return data
        
    def clear(self):
        for entry in self.fields.values():
            entry.delete(0, "end")
        self.msg_lbl.configure(text="")
