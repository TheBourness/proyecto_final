import customtkinter as ctk
from config import COLOR_PALETTE

class Sidebar(ctk.CTkFrame):
    """Menú lateral (Sidebar) estilo Notion/VSCode."""
    
    def __init__(self, parent, command_callback=None):
        super().__init__(parent, width=250, corner_radius=0, fg_color=COLOR_PALETTE["dark_gray"])
        self.command_callback = command_callback
        
        # Evitar que el frame cambie de tamaño si el texto es muy corto
        self.grid_propagate(False)
        
        self.title_label = ctk.CTkLabel(
            self, 
            text="BecaTrack", 
            font=ctk.CTkFont(family="Inter", size=24, weight="bold"),
            text_color=COLOR_PALETTE["blue"]
        )
        self.title_label.grid(row=0, column=0, padx=20, pady=(30, 30), sticky="w")
        
        self.buttons = []
        self._create_button("Dashboard", 1)
        self._create_button("Estudiantes", 2)
        self._create_button("Seguimientos", 3)
        self._create_button("Reportes", 4)
        self._create_button("Configuración", 5)
        
        # Espaciador para empujar el botón de Logout hacia abajo
        self.grid_rowconfigure(6, weight=1)
        
        self.logout_btn = ctk.CTkButton(
            self,
            text="Cerrar Sesión",
            fg_color="transparent",
            text_color=COLOR_PALETTE["red"],
            hover_color=COLOR_PALETTE["black"],
            anchor="w",
            font=ctk.CTkFont(size=14, weight="bold"),
            command=lambda: self.command_callback("Logout") if self.command_callback else None
        )
        self.logout_btn.grid(row=7, column=0, padx=20, pady=(20, 20), sticky="ew")

    def _create_button(self, text, row):
        btn = ctk.CTkButton(
            self, 
            text=text,
            fg_color="transparent",
            text_color=COLOR_PALETTE["text_primary"],
            hover_color=COLOR_PALETTE["black"],
            anchor="w",
            font=ctk.CTkFont(size=14),
            command=lambda t=text: self.command_callback(t) if self.command_callback else None
        )
        btn.grid(row=row, column=0, padx=20, pady=5, sticky="ew")
        self.buttons.append(btn)
