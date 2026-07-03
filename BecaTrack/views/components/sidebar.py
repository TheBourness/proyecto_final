import customtkinter as ctk
from config import COLOR_PALETTE

class Sidebar(ctk.CTkFrame):
    """Menú lateral estilizado con el tema claro."""
    def __init__(self, parent, command_callback=None):
        super().__init__(
            parent, 
            width=250, 
            corner_radius=0, 
            fg_color=COLOR_PALETTE["sidebar_bg"],
            border_width=1,
            border_color=COLOR_PALETTE["border"]
        )
        self.command_callback = command_callback
        self.grid_propagate(False)
        
        # Logo
        self.logo_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.logo_frame.grid(row=0, column=0, padx=20, pady=(30, 40), sticky="w")
        
        self.logo_icon = ctk.CTkLabel(self.logo_frame, text="🎓", font=ctk.CTkFont(size=24))
        self.logo_icon.pack(side="left", padx=(0,10))
        
        self.title_label = ctk.CTkLabel(
            self.logo_frame, 
            text="BecaTrack", 
            font=ctk.CTkFont(family="Inter", size=22, weight="bold"),
            text_color=COLOR_PALETTE["blue"]
        )
        self.title_label.pack(side="left")
        
        self.buttons = {}
        self._create_button("Dashboard", 1, icon="🏠", is_active=True)
        self._create_button("Directorio Becados", 2, icon="👥")
        self._create_button("Control de Seguimientos", 3, icon="📝")
        self._create_button("Métricas y Reportes", 4, icon="📊")
        self._create_button("Configuración", 5, icon="⚙️")
        
        self.grid_rowconfigure(6, weight=1)
        
        self.logout_btn = ctk.CTkButton(
            self,
            text="Cerrar Sesión",
            fg_color="transparent",
            text_color=COLOR_PALETTE["red"],
            hover_color=COLOR_PALETTE["red_light"],
            anchor="w",
            font=ctk.CTkFont(size=14, weight="bold"),
            command=lambda: self.command_callback("Logout") if self.command_callback else None
        )
        self.logout_btn.grid(row=7, column=0, padx=20, pady=(20, 20), sticky="ew")

    def _create_button(self, text, row, icon="", is_active=False):
        bg_color = COLOR_PALETTE["blue_light"] if is_active else "transparent"
        text_color = COLOR_PALETTE["blue"] if is_active else COLOR_PALETTE["text_secondary"]
        hover_color = COLOR_PALETTE["blue_light"] if is_active else COLOR_PALETTE["bg_app"]
        
        btn = ctk.CTkButton(
            self, 
            text=f"{icon}   {text}",
            fg_color=bg_color,
            text_color=text_color,
            hover_color=hover_color,
            anchor="w",
            height=45,
            corner_radius=8,
            font=ctk.CTkFont(size=14, weight="bold" if is_active else "normal"),
            command=lambda t=text: self._handle_click(t)
        )
        btn.grid(row=row, column=0, padx=20, pady=5, sticky="ew")
        self.buttons[text] = btn
        
    def _handle_click(self, view_name):
        for name, btn in self.buttons.items():
            if name == view_name:
                btn.configure(
                    fg_color=COLOR_PALETTE["blue_light"],
                    text_color=COLOR_PALETTE["blue"],
                    font=ctk.CTkFont(size=14, weight="bold")
                )
            else:
                btn.configure(
                    fg_color="transparent",
                    text_color=COLOR_PALETTE["text_secondary"],
                    font=ctk.CTkFont(size=14, weight="normal")
                )
        if self.command_callback:
            self.command_callback(view_name)
