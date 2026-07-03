import customtkinter as ctk
from config import COLOR_PALETTE

class LoginView(ctk.CTkFrame):
    """Vista de Login (UI) desarrollada en CustomTkinter."""
    
    def __init__(self, parent):
        super().__init__(parent, fg_color=COLOR_PALETTE["black"])
        
        self.parent = parent
        self._setup_ui()

    def _setup_ui(self):
        # Contenedor central (tarjeta de login con diseño moderno)
        self.card = ctk.CTkFrame(
            self, 
            fg_color=COLOR_PALETTE["dark_gray"], 
            corner_radius=15, 
            width=400, 
            height=500
        )
        self.card.place(relx=0.5, rely=0.5, anchor="center")
        
        # Título principal
        self.title_label = ctk.CTkLabel(
            self.card, 
            text="BecaTrack", 
            font=ctk.CTkFont(family="Inter", size=32, weight="bold"),
            text_color=COLOR_PALETTE["blue"]
        )
        self.title_label.place(relx=0.5, rely=0.15, anchor="center")
        
        # Subtítulo
        self.subtitle = ctk.CTkLabel(
            self.card, 
            text="Sistema de Monitoreo", 
            font=ctk.CTkFont(size=14),
            text_color=COLOR_PALETTE["text_secondary"]
        )
        self.subtitle.place(relx=0.5, rely=0.22, anchor="center")

        # Input de Usuario
        self.username_entry = ctk.CTkEntry(
            self.card, 
            placeholder_text="Usuario", 
            width=300, 
            height=45,
            corner_radius=8,
            border_color=COLOR_PALETTE["border"],
            fg_color=COLOR_PALETTE["black"],
            text_color=COLOR_PALETTE["text_primary"]
        )
        self.username_entry.place(relx=0.5, rely=0.4, anchor="center")
        
        # Input de Contraseña
        self.password_entry = ctk.CTkEntry(
            self.card, 
            placeholder_text="Contraseña", 
            show="*", 
            width=300, 
            height=45,
            corner_radius=8,
            border_color=COLOR_PALETTE["border"],
            fg_color=COLOR_PALETTE["black"],
            text_color=COLOR_PALETTE["text_primary"]
        )
        self.password_entry.place(relx=0.5, rely=0.55, anchor="center")
        
        # Botón para Mostrar/Ocultar contraseña (posicionado a la derecha del input)
        self.toggle_password_btn = ctk.CTkButton(
            self.card, 
            text="Mostrar", 
            width=60, 
            height=30,
            fg_color="transparent",
            text_color=COLOR_PALETTE["blue"],
            hover_color=COLOR_PALETTE["black"]
        )
        self.toggle_password_btn.place(relx=0.78, rely=0.55, anchor="center")

        # Botón Ingresar
        self.login_button = ctk.CTkButton(
            self.card, 
            text="Ingresar", 
            width=300, 
            height=45,
            corner_radius=8,
            fg_color=COLOR_PALETTE["blue"],
            hover_color="#1D4ED8",
            font=ctk.CTkFont(size=15, weight="bold")
        )
        self.login_button.place(relx=0.5, rely=0.75, anchor="center")
        
        # Label para mostrar mensajes de error o éxito
        self.message_label = ctk.CTkLabel(
            self.card, 
            text="", 
            font=ctk.CTkFont(size=13, weight="bold")
        )
        self.message_label.place(relx=0.5, rely=0.88, anchor="center")

    def show_error(self, message: str):
        self.message_label.configure(text=message, text_color=COLOR_PALETTE["red"])

    def show_success(self, message: str):
        self.message_label.configure(text=message, text_color=COLOR_PALETTE["green"])
