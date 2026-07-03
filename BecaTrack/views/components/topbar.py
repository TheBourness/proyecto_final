import customtkinter as ctk
from config import COLOR_PALETTE

class Topbar(ctk.CTkFrame):
    """Barra superior que muestra el título de la sección y el usuario activo."""
    
    def __init__(self, parent, user_name="Admin"):
        super().__init__(parent, height=60, corner_radius=0, fg_color=COLOR_PALETTE["black"])
        self.grid_propagate(False)
        
        self.grid_columnconfigure(0, weight=1)
        
        # Título de la sección actual
        self.section_title = ctk.CTkLabel(
            self, 
            text="Dashboard", 
            font=ctk.CTkFont(family="Inter", size=20, weight="bold"),
            text_color=COLOR_PALETTE["text_primary"]
        )
        self.section_title.grid(row=0, column=0, padx=20, pady=15, sticky="w")
        
        # Información del usuario
        self.user_label = ctk.CTkLabel(
            self,
            text=f"👤 {user_name}",
            font=ctk.CTkFont(size=14),
            text_color=COLOR_PALETTE["text_secondary"]
        )
        self.user_label.grid(row=0, column=1, padx=20, pady=15, sticky="e")

    def set_section(self, title: str):
        self.section_title.configure(text=title)
